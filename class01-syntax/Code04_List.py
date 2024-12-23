li = ["a", "b", 121, "hello"]
print(li[1])  # b
print(li[-2])  # 121
# print(li[10])  # IndexError: list index out of range
print("*" * 50)

# 列表的遍历
for i in li:
    print(i)

print("*" * 50)

i = 0
while i < len(li):
    print(li[i])
    i += 1

print("*" * 50)

# 列表添加数据
language = ["Python", "Java", "C++"]
numList = [1990, 1222, 5554]
language = language + numList
print(language)  # ['Python', 'Java', 'C++', 1990, 1222, 5554]
# insert
language = ["Python", "Java", "C++"]
language.insert(1, "Go")
language.insert(10, "C#")
language.insert(-1, "JS")
language.insert(-10, "html")
print(language)  # ['html', 'Python', 'Go', 'Java', 'C++', 'JS', 'C#']
t = ("Shell", "C")
language.insert(0, t)
print(language)  # [('Shell', 'C'), 'html', 'Python', 'Go', 'Java', 'C++', 'JS', 'C#']
# append
language.append("中文")
# extend
li1 = ["aaa", "bbb"]
li2 = ["ddd", "tttt"]
li1.append(li2)
print(li1)  # ['aaa', 'bbb', ['ddd', 'tttt']]
li1.extend(li2)
print(li1)  # ['aaa', 'bbb', ['ddd', 'tttt'], 'ddd', 'tttt']

print("*" * 50)

# 修改元素
# 修改单个元素
breakfast = ["豆浆", "油条"]
breakfast[0] = "豆腐脑"
print(breakfast)
# 修改一组元素
breakfast = ["豆浆", "油条", "包子", "馒头"]
breakfast[1:4] = ["鸡蛋"]
print(breakfast)  # ['豆浆', '鸡蛋']
# 对空切片赋值操作
breakfast = ["豆浆", "油条", "包子", "馒头"]
breakfast[2:2] = ["鸡蛋"]
print(breakfast)  # ['豆浆', '油条', '鸡蛋', '包子', '馒头']

print("*" * 50)

# 删除元素
r = list("hello")
print(r)  # ['h', 'e', 'l', 'l', 'o']
del r[0]
print(r)  # ['e', 'l', 'l', 'o']
del r[0:2]  # 左闭右开
print(r)  # ['l', 'o']
# del r
# print(r)  # NameError: name 'r' is not defined

# pop
nums = [1, 2, 3, 4, 5]
p = nums.pop()
print(p)  # 5
print(nums)  # [1, 2, 3, 4]

# remove
mm = ["Hello", "world", "you"]
mm.remove("you")
print(mm)  # ['Hello', 'world']

# clear
mm = ["Hello", "world", "you"]
mm.clear()
print(mm)  # []

# 查找元素
find = ["Hello", "world", "you"]
print("he" in find)  # False
print("you" in find)  # True
print("lla" not in find)  # True
# count
# index
# print(find.index("he"))  # ValueError: 'he' is not in list

# 排序
kk = [1, 2, 3, 4]
kk.reverse()
print(kk)  # [4, 3, 2, 1]

# sort
hh = [5, 2, 65, 4, 8, 1]
hh.sort()  # 默认从小到大
print(hh)  # [1, 2, 4, 5, 8, 65]
hh.sort(reverse=True)  # 从大到小
print(hh)  # [65, 8, 5, 4, 2, 1]

# sorted
ff = [1, 4, 2, 9, 3]
ff1 = sorted(ff)
print(ff)  # [1, 4, 2, 9, 3]
print(ff1)  # [1, 2, 3, 4, 9]

# 列表推导式
# 给列表中的每个元素都乘以2
dd = [1, 2, 3, 4]
print([i * 2 for i in dd])  # [2, 4, 6, 8]
