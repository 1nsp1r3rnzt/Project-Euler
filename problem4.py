# program to find maximum palindromic for a three digit numbers
# for two
fac=[]
def max_palindromic(digit):
	minimumrange=pow(10,digit-1)
	maximumrange=pow(10,digit)-1

	for i in range(minimumrange,maximumrange+1):
		for j in range(minimumrange,maximumrange+1):
			currentnumber=i*j
			
			reversednumber = ''.join(item[1] for item in sorted(enumerate(str (currentnumber)), reverse=True))
			if(str(currentnumber)==reversednumber):
				fac.append(currentnumber)
	return max(fac)		
print (max_palindromic(3))

