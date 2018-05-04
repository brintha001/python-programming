lst = []
Y= int(input('How many numbers: '))
for n in range(N):
    num = int(input('Enter number '))
    lst.append(num)
print max(lst), min(lst)
