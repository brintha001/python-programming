store = []
amount = int(input("please enter the amount of numbers you want to sort "))
for a in range(amount):
   num = int(input("please enter a number "))
   store.append(num)
c=sorted(store)
print (c)
print (c[1])
