u,v=raw_input().split()
u=int(u)
v=int(v)
r=0
while(r<u):
	if (v**r)==a:
		print("yes")
		break
	else:
		r=r+1
if r==u:
	print("no")
