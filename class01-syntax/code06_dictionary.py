# 定义字典
# dic1 = {}
# dic2 = {"name": "ll", "age": 18}
dic3 = dict()

# 添加元素
dic3["id"] = 1
dic3["name"] = "Lucy"
print(dic3)  # {'id': 1, 'name': 'Lucy'}

# 修改元素
dic3["name"] = "Peter"
print(dic3)  # {'id': 1, 'name': 'Peter'}

# 查找
print(dic3["name"])  # Peter

# 删除元素
del dic3["name"]
print(dic3)  # {'id': 1}

# 清空字典
dic3.clear()
print(dic3)  # {}

# 常用操作
map = {"id": 2, "age": 20, "name": "MyName"}
print(len(map))  # 3

print("*" * 50)

keys = map.keys()
for k in keys:
    print(k)
print("*" * 50)
values = map.values()
for v in values:
    print(v)
print("*" * 50)
items = map.items()
for key, value in items:
    print(key, value)
