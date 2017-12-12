fact=[]
def fac(limt_number):
	n=2
	while(n<=limt_number):
		foundfactorial=0
		while(limt_number%n==0):
			foundfactorial=1
			limt_number=limt_number/n
		if(foundfactorial==1):
			fact.append(n)
		n=n+1
	return 1

fac(600851475143)
print max(fact)
