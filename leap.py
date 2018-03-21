year=int(input("Enter the year:"))
if year %4==0 & year %100!=0:
    print("yes")
elif year %100==0:
    print("no")
elif year %400==0:
    print("yes")
else:
    print("no")
