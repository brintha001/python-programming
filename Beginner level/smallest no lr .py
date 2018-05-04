a,c=raw_input().split()
a=int(a)
c=int(c)
if a%c==0:
	print a
elif c%a==0:
	print c
else:
	print a*c
