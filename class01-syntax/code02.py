"""
运算符
"""
import random

print(9 / 2)  # 4.5
print(9 // 2)  # 4
print(2 ** 3)

"""
类型转换
"""
# 字符串转整数 int(str)
str1 = "124"
print(type(int(str1)))
# 数值转字符串 str(num)
num = 1.3
print(type(str(num)))

"""
输入
"""
# name = input("请输入你的名字：")
# print("name的值{}, name的类型{}".format(name, type(name)))
# num = input("请输入一个整数：")

"""
if语句
"""
# if int(num):
#     print(type(num))
#     print("这是一个整数%d" % (int(num)))
# elif float(num):
#     print("这是一个浮点数%f" % (float(num)))
# else:
#     print("输入的内容为{}".format(num))

score = 50
if score >= 80:
    print("优秀")
elif 60 <= score < 80:
    print("及格")
else:
    print("不及格")

"""
random类
"""
# 随机生成[0,1)之间的浮点数
print(random.random())
# 随机生成[0,2]范围内整数，也就是随机输出0、1、2
print(random.randint(0, 2))
# random.randrange(a,b,step)
print(random.randrange(0, 11, 2))
# 随机生成[0,3]之间的浮点数
print(random.uniform(0, 3))
# 随机输出”石头“、”剪刀“、”布“
myList = ["石头", "剪刀", "布"]
print(random.choice(myList))

# i = 0
# while i < 10:
#     print(f"i= {i}")
#     if i % 2 == 0:
#         print(f"这是偶数：{i}")
#     i += 1

# 打印九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print(f"{row}*{col}={row * col}", end="\t")
        col += 1
    print("")
    row += 1

"""
range函数
"""
for i in range(5):
    print(i)
# 求1——100累加和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
