import sys

def main():

	print(""" 
	   		1. Negation (NOT)
			2. Conjunction (AND)
	   		3. Disjunction (OR)
	   		4. Implicaton
	   		5. Bi-implication
	   		6. Exclusive OR
	   		7. Exit the program
		""")
	
	lo = int(input("choose logical operator by typing a number between 1 and 7: "))

	match lo:
		case 1:
			print("You have chosen negation.")
			print("p	a")
			for p in [True, False]:
				a = negation(p)
				print(p,a)
	
		case 2:
			print("You have chosen conjunction (AND).")
			print("p    q    p and q")
			for p in [True, False]:
				for q in [True, False]:
					a = conjunction(p,q)
					print(p,q,a)


		case 3:
			print("You have chosen disjunction (OR)")
			print("p    q    p or q")
			for p in [True, False]:
				for q in [True, False]:
					a = disjunction(p,q)
					print(p,q,a)
		
		case 4:
			print("You have chosen implication")
			print("p	q	a")
			for p in [True, False]:
				for q in [True, False]:
					a = implication(p,q)
					print(p,q,a)

		
		case 5:
			print("You have chosen bi-implication")
			print("p	q	a")
			for p in [True, False]:
				for q in [True, False]:
					a = bi_implication(p, q)
					print(p, q, a)
	

		case 6:
			print("p	q	a")
			for p in [True, False]:
				for q in [True, False]:	
					a = exclusive_disjunction(p, q)
					print(p, q, a)

		case 7:
			sys.exit()
		
	main()

def disjunction(p, q):
	return p or q

def conjunction(p, q):
	return p and q

def negation(p):
	return not p

def implication(p,q):
	return not p or q

def bi_implication(p,q):
	return (not p or q) and (not q or p)

def exclusive_disjunction(p, q):
	return (p and not q) or (not p and q)

if __name__== "__main__":
	main()