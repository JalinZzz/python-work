#  例如{"username":"admin","passwd":"123456"}
#  # 1.设计1个登录的程序， 不同的用户名和成对密码存在个字典里面， 输入正确的用户名和密码去登陆，
#   # 2.首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名  
#  3.当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应， 则提示密码错误请重新输入。
#  # 4.如果密码输入错误超过三次，中断程序运行。
#   # 5.当输入密码错误时，提示还有几次机会
#  6用户名和密码都输入正确的时候，提示登陆成功!


dic = {"username": "admin", "passWd": "123456"}
i = 3
while True:
    username = input('please input your username:')
    if dic['username'] == username:
        while i > 0:
            passWd = input('please input your passWd:')
            if dic['passWd'] == passWd:
                print('登录成功')
                break
            else:
                i = i - 1
                if i > 0:
                    print('just for' + str(i))
        print('over')
        break
    else:
        print('x')
