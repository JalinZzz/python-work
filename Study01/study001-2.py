# 字符串拼接，字符串切片、取值，格式化输出、元组、列表

a='hello'
age=20

#
# print(a)
# print(a,age)
# print(a + str(age))

# print(a[-3:-1])
# print(a[2:4])
# print(a[0:])

# print('this is girl %d'%age)
# print('this is girl %s,and %d'%(a,age))
# print('this is girl {0},and {1}'.format(a,age))



#########元组


b=(12,'hello',(3,7,9,12,16),9.89,[2,3,4,5])
# print(type(b))
# print(b)
# print(b[2][-2])
# print(b[len(b)-1])
# print(b[2])
# b[-1][-1]='Tiger'————————#元组内列表里面的元素可修改，但整个列表作为元组的一个元素不可修改
# print(b)



########列表

c=[12,'hello',(3,7,9,12,16),9.89,['hello','python']]

# print(c[-1][-1][0])
c[2]='Tiger'
c[-1].append('baidu')
print(c)
