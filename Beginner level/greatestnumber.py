u=int(input())
v=int(input())
if(u<=100000 and v<=100000):
  while(u!=v):
    if(u>v):
      u-=v
    else:
        v-=u
  print(u)
