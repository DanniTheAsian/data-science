import re
import itertools
import random
from typing import List, Tuple, Dict, Set, Union

# -----------------------------
# Tokenizer + Parser (recursive descent)
# -----------------------------
TOK_REGEX = re.compile(r"""
    (\s+)                                     | # whitespace
    (<=|>=|==|=>|-->|⟹)                       | # multi-char implies tokens
    (⊆|⊂|∪|∩|¬|∅|Ø|\\|-|\||&|\^|'|\(|\)|=|,|:) | # single char tokens
    ([A-Za-z][A-Za-z0-9_]*)                   | # identifiers
    (NOT|AND|OR|IMPLIES|SUBSET|EMPTY|UNIVERSAL)  # keywords
""", re.VERBOSE | re.IGNORECASE)


def tokenize(s: str) -> List[str]:
    tokens = []
    idx = 0
    while idx < len(s):
        m = TOK_REGEX.match(s, idx)
        if not m:
            if s[idx].isspace():
                idx += 1
                continue
            tokens.append(s[idx])
            idx += 1
            continue
        token = next((g for g in m.groups() if g and not g.isspace()), None)
        if token is not None:
            tokens.append(token)
        idx = m.end()
    normalized = []
    for t in tokens:
        if re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', t) and t.upper() in {"NOT", "AND", "OR", "IMPLIES", "SUBSET", "EMPTY", "UNIVERSAL"}:
            normalized.append(t.upper())
        else:
            normalized.append(t)
    return normalized


# -----------------------------
# AST node classes
# -----------------------------
class Node:
    def vars(self) -> Set[str]:
        raise NotImplementedError
    def eval(self, env: Dict[str, bool]) -> bool:
        raise NotImplementedError
    def __repr__(self): return self.__str__()


class Var(Node):
    def __init__(self, name: str): self.name = name
    def vars(self): return {self.name}
    def eval(self, env):
        if self.name == 'U': return True
        if self.name == '∅': return False
        return bool(env[self.name])
    def __str__(self): return self.name


class Const(Node):
    def __init__(self, value: bool): self.value = value
    def vars(self): return set()
    def eval(self, env): return self.value
    def __str__(self): return 'U' if self.value else '∅'


class Not(Node):
    def __init__(self, child: Node): self.child = child
    def vars(self): return self.child.vars()
    def eval(self, env): return not self.child.eval(env)
    def __str__(self): return f'¬({self.child})'


class And(Node):
    def __init__(self, left: Node, right: Node): self.left, self.right = left, right
    def vars(self): return self.left.vars() | self.right.vars()
    def eval(self, env): return self.left.eval(env) and self.right.eval(env)
    def __str__(self): return f'({self.left} ∩ {self.right})'


class Or(Node):
    def __init__(self, left: Node, right: Node): self.left, self.right = left, right
    def vars(self): return self.left.vars() | self.right.vars()
    def eval(self, env): return self.left.eval(env) or self.right.eval(env)
    def __str__(self): return f'({self.left} ∪ {self.right})'


class Diff(Node):
    def __init__(self, left: Node, right: Node): self.left, self.right = left, right
    def vars(self): return self.left.vars() | self.right.vars()
    def eval(self, env): return self.left.eval(env) and not self.right.eval(env)
    def __str__(self): return f'({self.left} - {self.right})'


# -----------------------------
# Parser
# -----------------------------
class Parser:
    def __init__(self, tokens: List[str]): self.toks, self.pos = tokens, 0
    def peek(self): return self.toks[self.pos] if self.pos < len(self.toks) else None
    def pop(self): t = self.peek(); self.pos += 1; return t
    def parse_expression(self) -> Node: return self.parse_or()

    def parse_or(self):
        node = self.parse_and()
        while self.peek() in ('OR', '∪', '|'):
            self.pop(); rhs = self.parse_and()
            node = Or(node, rhs)
        return node

    def parse_and(self):
        node = self.parse_diff()
        while self.peek() in ('AND', '∩', '&'):
            self.pop(); rhs = self.parse_diff()
            node = And(node, rhs)
        return node

    def parse_diff(self):
        node = self.parse_unary()
        while self.peek() in ('-', '\\', 'DIFF'):
            self.pop(); rhs = self.parse_unary()
            node = Diff(node, rhs)
        return node

    def parse_unary(self):
        t = self.peek()
        if t in ('NOT', '¬', '^'):
            self.pop(); return Not(self.parse_unary())
        if t and re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", t):
            self.pop()
            name = t.upper()
            if name == 'EMPTY': return Const(False)
            if name in ('UNIVERSAL', 'U'): return Const(True)
            return Var(t)
        if t == '(':
            self.pop()
            node = self.parse_expression()
            if self.peek() == ')': self.pop()
            else: raise ValueError("Mangler ')'")
            return node
        if t == '∅': self.pop(); return Const(False)
        if t == 'U': self.pop(); return Const(True)
        raise ValueError(f"Uventet token: {t} (pos {self.pos})")


# -----------------------------
# Normalizer
# -----------------------------
def normalize_statement_text(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\bNOT\b", "¬", s, flags=re.IGNORECASE)
    s = re.sub(r"'", " ¬ ", s)
    s = re.sub(r"\bAND\b", "∩", s, flags=re.IGNORECASE)
    s = re.sub(r"\bOR\b", "∪", s, flags=re.IGNORECASE)
    s = re.sub(r"\bSUBSET\b", "⊆", s, flags=re.IGNORECASE)
    s = re.sub(r"\bIMPLIES\b", "⟹", s, flags=re.IGNORECASE)
    s = re.sub(r"=>|-->", "⟹", s)
    s = re.sub(r"\bEMPTY\b", "∅", s, flags=re.IGNORECASE)
    s = re.sub(r"\bUNIVERSAL\b", "U", s, flags=re.IGNORECASE)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r'([A-Za-z0-9_]+)\s+¬', r'¬ \1', s)
    return s


# -----------------------------
# Utility: Evaluate equivalence
# -----------------------------
def collect_vars(nodes: List[Node]) -> List[str]:
    vs = set()
    for n in nodes: vs |= n.vars()
    vs.discard('U'); vs.discard('∅')
    return sorted(vs)

def all_envs(varlist: List[str]):
    for bits in itertools.product([False, True], repeat=len(varlist)):
        yield dict(zip(varlist, bits))

def random_envs(varlist: List[str], k=2000):
    for _ in range(k):
        yield dict(zip(varlist, [random.choice([False, True]) for _ in varlist]))

def expressions_equal(e1: Node, e2: Node, limit_vars_check=10) -> Tuple[bool, Union[None, Dict[str,bool]]]:
    vs = collect_vars([e1, e2])
    if len(vs) > limit_vars_check:
        for env in random_envs(vs, k=2000):
            if e1.eval(env) != e2.eval(env):
                return False, env
        return None, None
    for env in all_envs(vs):
        if e1.eval(env) != e2.eval(env):
            return False, env
    return True, None


# -----------------------------
# High-level checker
# -----------------------------
def parse_expr_from_text(text: str) -> Node:
    text = normalize_statement_text(text)
    tokens = tokenize(text)
    return Parser(tokens).parse_expression()

def implies(e1: Node, e2: Node, limit_vars_check=10) -> Tuple[bool, Union[None, Dict[str,bool]]]:
    # e1 => e2 iff for all env: not e1 or e2
    vs = collect_vars([e1, e2])
    if len(vs) > limit_vars_check:
        for env in random_envs(vs, k=2000):
            if e1.eval(env) and not e2.eval(env):
                return False, env
        return None, None
    else:
        for env in all_envs(vs):
            if e1.eval(env) and not e2.eval(env):
                return False, env
        return True, None


def check_statement(statement: str):
    """
    Forståer og tjekker:
      - kædede ligheder:  A = B = C
      - implikation:      <venstre> IMPLIES <højre>
      - kombination:       (A=B=C) IMPLIES (D=E)
    Returnerer (True/False/None, besked).
    """
    s = statement.strip()
    s_norm = s.replace('<=', '⊆').replace('SUBSET', '⊆').replace('IMPLIES', '⟹')

    # 1) Hvis der er en implikation, del i præmis og konsekvens (kun første implikation)
    impl_match = re.search(r'(⟹|=>|-->)', s_norm)
    if impl_match:
        left_part = s_norm[:impl_match.start()].strip()
        right_part = s_norm[impl_match.end():].strip()

        # Tjek kædede = på hver side separat
        left_parts = [p.strip() for p in re.split(r'(?:=|⊆)', left_part) if p.strip()]
        right_parts = [p.strip() for p in re.split(r'(?:=|⊆)', right_part) if p.strip()]

        if not left_parts or not right_parts:
            return None, "Forkert form: forventer udtryk på begge sider af 'IMPLIES'."

        # Parse og tjek venstre kæde
        try:
            left_nodes = [parse_expr_from_text(p) for p in left_parts]
            right_nodes = [parse_expr_from_text(p) for p in right_parts]
        except Exception as e:
            return None, f"Fejl ved parsing: {e}"

        # kræv at alle led i venstre kæde er ækvivalente
        for i in range(len(left_nodes) - 1):
            eq, counter = expressions_equal(left_nodes[i], left_nodes[i + 1])
            if eq is False:
                return False, f"Venstre kæde falsk: {left_parts[i]} ≠ {left_parts[i+1]}. Modeksempel: {counter}"
            if eq is None:
                return None, f"Kan ikke afgøre venstre kæde mellem {left_parts[i]} og {left_parts[i+1]} (sampling)."

        # kræv at alle led i højre kæde er ækvivalente
        for i in range(len(right_nodes) - 1):
            eq, counter = expressions_equal(right_nodes[i], right_nodes[i + 1])
            if eq is False:
                return False, f"Højre kæde falsk: {right_parts[i]} ≠ {right_parts[i+1]}. Modeksempel: {counter}"
            if eq is None:
                return None, f"Kan ikke afgøre højre kæde mellem {right_parts[i]} og {right_parts[i+1]} (sampling)."

        # Nu har vi: (venstre-kæde gælder som en samlet lighed) ⟹ (højre-kæde gælder)
        # Vi skal tjekke at (venstre_expr) => (højre_expr) holder for alle tildelinger.
        # Brug første led i hver kæde som repræsentant (de er ækvivalente pga. ovenfor)
        left_node = left_nodes[0]
        right_node = right_nodes[0]
        impl_holds, counter = implies(left_node, right_node)
        if impl_holds is True:
            return True, f"Implikation sand: ({' = '.join(left_parts)}) ⟹ ({' = '.join(right_parts)})."
        elif impl_holds is False:
            return False, f"Implikation falsk. Modeksempel: {counter}"
        else:
            return None, "Ikke afgørende for implikationen (sampling)."

    # 2) Hvis ingen implikation: håndtér som før — split på = / ⊆ og tjek kæden
    parts = re.split(r'(?:=|⊆)', s_norm)
    parts = [p.strip() for p in parts if p.strip()]

    if len(parts) < 2:
        return None, "Udsagnet skal indeholde mindst én '=' eller '⊆'."

    try:
        nodes = [parse_expr_from_text(p) for p in parts]
    except Exception as e:
        return None, f"Fejl ved parsing: {e}"

    for i in range(len(nodes) - 1):
        eq, counter = expressions_equal(nodes[i], nodes[i + 1])
        if eq is False:
            return False, f"{parts[i]} ≠ {parts[i+1]} (FALSK). Modeksempel: {counter}"
        if eq is None:
            return None, f"Ikke afgørende mellem {parts[i]} og {parts[i+1]} (sampling)."

    return True, f"Alle led ({' = '.join(parts)}) er ækvivalente (SAND)."


# -----------------------------
# CLI
# -----------------------------
def main():
    print("="*60)
    print("MÆNGDETEORI - FORBEDRET KONTROLLER")
    print("Skriv udsagn af formen: 'A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)'")
    print("="*60)
    while True:
        s = input("Indtast udsagn (eller 'exit'): ").strip()
        if s.lower() in ('exit', 'quit', 'q'):
            print("Farvel!")
            break
        if not s:
            continue
        result, msg = check_statement(s)
        print(msg)


if __name__ == "__main__":
    main()
