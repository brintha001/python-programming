c=int(raw_input())
d=raw_input().split()
count=0
g=c
i=0
s=0
while (c>1):
	if int(d[i])<=int(d[i+1]):
		count=count+1
		i=i+1
		c=c-1
	else:
		s=s+1
		i=i+1
		c=c-1
if count==g-1:
	print "yes"
else:
	print "no"
