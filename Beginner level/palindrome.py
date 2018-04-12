numb=raw_input()
if numb.isdigit():
	numb=int(numb)
	v = numb
	sum=0
	while(numb!=0):
		a=numb%10
		sum=sum*10+a
		numb=numb/10
	if(sum==v):
		print("yes")
	else:
		print("no")
else:
	print("Invalid")
