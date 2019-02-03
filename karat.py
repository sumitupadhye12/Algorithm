def karrat(num1,num2):
	if(len(num1)==1):
		return(int(num1)*int(num2))
	tm = len(num1)//2
	a = int(num1[0:tm])
	b = int(num1[tm:tm*2])
	tm = len(num2)//2
	c = int(num2[0:tm])
	d = int(num2[tm:tm*2])
	ac = int(karrat(str(a),str(c)))
	bd = int(karrat(str(b),str(d)))
	tm = int(karrat(str(a+b),str(c+d)))
	tm = tm -ac-bd
	last = (ac*(10**len(num1)))+(tm * (10**(len(num1)/2)))+bd
	return(last)

if __name__ == "__main__":
	num1 = input("Enter the first number:")
	num2 = input("Enter the second number:")
	print(karrat(str(num1),str(num2)))