price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])


interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])


interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))


interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))


interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))


string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)


data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))
print(data)
data.sort()
print(data)





