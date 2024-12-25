# 元组的定义
tup = (1, 3, 4)
# 定义单个元素的元组时要加逗号
tup1 = (1)
print(type(tup1))  # <class 'int'>
tup1 = (1,)
print(type(tup1))  # <class 'tuple'>
# len
print(len(tup1))  # 1

# 元组”可变“的情况
tt = (3, 5, [99, 88, 77], 6)
tt[2][0] = 66
print(tt)  # (3, 5, [66, 88, 77], 6)
