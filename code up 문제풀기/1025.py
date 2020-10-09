# a = 10000
# c = b % a
# d = b - c
# print('['+str(d)+']')
#
#
# a = 1000
# b = c
# c = b % a
# d = b - c
# print('['+str(d)+']')
#
# a = 100
# b = c
# c = b % a
# d = b - c
# print('['+str(d)+']')
#
# a = 10
# b = c
# c = b % a
# d = b - c
# print('['+str(d)+']')
#
#
# a = 1
# b = c
# c = b % a
# d = b - c
# print('['+str(d)+']')
b = int(input())
a = 10000
i = 0
while i < 5:
    c = b % a
    d = b - c
    print('[' + str(d) + ']')
    a = a // 10
    i += 1
    b = c
