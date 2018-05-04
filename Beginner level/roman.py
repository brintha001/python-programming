v=raw_input()
w=len(v)
x=0
y=w
if (v=='IX'):
	print "9"
if (v=='IIX'):
	print "19"
else:
	while(y>0):
		for i in range(0,w):
			if(v[i]=='I'):
				x=x+1
				y=y-1
			elif(v[i]=='X'):
				x=x+10
				y=y-1
			elif(v[i]=='V'):
				x=x+5
				y=y-1
	print s
