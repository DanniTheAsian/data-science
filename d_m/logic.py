

def main():
	print("p    q    r")
	for p in [True, False]:
		for q in [True, False]:
			a = disjunction(p,q)
			print(p,q,a)

def disjunction(p, q):
	return p or q

if __name__=="__main__":
	main()