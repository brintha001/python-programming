N=int(input("Enter number: "))
rev=1
while(N>1):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of given number is:",rev)
