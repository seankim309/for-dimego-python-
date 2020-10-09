#1
# def is_odd(a):
#     if a % 2 == 0:
#         print('짝수입니다.')
#     else:
#         print('홀수입니다.')
# is_odd(3)

#2
# def a(*args):
#     b = 0
#     for i in args:
#         b += i
#     return b / len(args)
#
# print(a(1, 2, 3, 4, 5, 6, 7, 8, 9))


#3
# input1 = int(input("첫번째 숫자를 입력하세요:"))
# input2 = int(input("두번째 숫자를 입력하세요:"))
#
# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)

#4
#(3)

#5
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
#
# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close()

#6
# a = input()
# f1 = open("test.txt", 'a')
# f1.write(a)
# f1.close()

#7 !!!!!!!!!!!!!!!!!!!!
# f1 = open("test.txt", 'r')
# a = f1.read()
# b = a.replace('java', 'python')
# f1.close()
#
# f2 = open("test.txt", 'w')
# f2.write(b)
# f2.close()