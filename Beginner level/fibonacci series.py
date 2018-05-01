n=raw_input()
n=int(n)
e=1
d=1
f=0
print e,
print d,
for i in range(1,n-1):
        f=e+d
        print f,
        e=d
        d=f
