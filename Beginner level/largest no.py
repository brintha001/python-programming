numb1=raw_input()
numb2=raw_input()
numb3=raw_input()
if isinstance(numb1,str) and isinstance(numb2,str) and isinstance(numb3,str):
	if(((numb1>='a') and (numb1<='z')) and ((numb2>='a') and (numb2<='z')) and ((numb3>='a') and (numb3<='z'))):
		print("Invalid")
	else:
		numb1=int(numb1)
		numb2=int(numb2)
		numb3=int(numb3)
		if(numb1>=numb2 and numb1>=numb3):
			print(numb1)
		elif(numb2>=numb1 and numb2>=numb3):
			print(numb2)
		else:
			print(numb3)

else:
	print("Invalid")
