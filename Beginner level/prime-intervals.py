x,y=raw_input().split()
x=int(x)
y=int(y)
for num in range(l,y+1):
	      if num>1:
		           for i in range(2,num):
			               if(num % i) == 0:
				                     break
	           	else:
			              print num,
           
