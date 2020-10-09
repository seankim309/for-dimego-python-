a = int(input())
b = 10000
while b > 0:
    n = a % b
    m = a - n
    print('['+ str(m) +']')
    a = n
    b = b // 10