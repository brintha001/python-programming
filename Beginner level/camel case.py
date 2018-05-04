a=raw_input().split()
d=[]
r=[]
for i in a:
  for j in i:
    if(j==j.lower()):
      s=j.upper()
      d.append(s)
    else:
      s=j.lower()
      d.append(s)
  n="".join(d)
  print n,
  d=[]
   
