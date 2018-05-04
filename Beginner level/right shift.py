m,s=input().split()
m=int(m)
s=int(s)
g=s
b=input().split()
if(m>s);
    while(s>0):
        f=b[-s]
        print(f,end=' ')
        s=s-1
    c=m-g
    for u in range(1,c):
        print(b[u],end=' ')
else:
    print(b)       
