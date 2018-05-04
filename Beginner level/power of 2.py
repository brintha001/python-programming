def Power(b):
    if (b == 0):
        return False
    while (b != 1):
            if (b % 2 != 0):
                return False
            b = b // 2
             
    return True
n=int(input())
if(Power(n)):
    print('Yes')
else:
    print('No')
