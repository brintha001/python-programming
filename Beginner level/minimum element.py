list = []
num = int(input('how many number'))
for n in range(num):
    numbers = int(input('enter number'))
    list.append(numbers)
print("Minimum element in the list is :", min(list))
