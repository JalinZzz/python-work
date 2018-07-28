n = 10
x = 0
while n > 0:
    age = int(input('please input your age:'))
    sex = str(input('please input your sex:'))
    if 10 <= age <= 12 and sex == 'f':
        x += 1
        print('ok')
    n -= 1
print(x)
