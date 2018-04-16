a=int(input())
m=0
for i in range(2,a//2+1):
    if(a%i==0):
    m=m+1
if(m<=0):
    print("yes")
else:
    print("no")
