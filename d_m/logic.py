

def main():

	print("""
	   		1. negation (NOT)
			2. conjunction (AND)
	   		3. disjunction (OR)
	   		4. exclusive OR
		""")
	
	lo = int(input("choose logical operator: "))

	match lo:
		case 1:
			print("p	a")
			for p in [True, False]:
				a = negation(p)
				print(p,a)
			main()
		case 2:
			print("You have chosen conjunction (AND)")
			print("p    q    p and q")
			for p in [True, False]:
				for q in [True, False]:
					a = conjunction(p,q)
					print(p,q,a)
			main()
		case 3:
			print("You have chosen disjunction (OR)")
			print("p    q    p or q")
			for p in [True, False]:
				for q in [True, False]:
					a = disjunction(p,q)
					print(p,q,a)
			main()
		
		case 4:
			print("p	q	a")
			for p in [True, False]:
				for q in [True, False]:	
					a = exclusive_disjunction(p, q)
					print(p, q, a)


def disjunction(p, q):
	return p or q

def conjunction(p, q):
	return p and q

def negation(p):
	return not p

def exclusive_disjunction(p, q):
	return (p and not q) or (not p and q)

if __name__=="__main__":
	main()