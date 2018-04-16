num=raw_input()
if num.isdigit():
        num=int(num)
        power=len(str(num))
        sum=0
        c=num
        while c>0:
               digit=c%10
               sum=sum+digit**power
               c=c/10
        if(sum==num):
               print("yes")
        else:
               print("no")
  else:
          print("invalid")
            
