import re

pattern = r'\b[sS]\w*'  # \b: 匹配单词边界。[sS]: 匹配大小写字母 s 或 S。\w*: 匹配 0 个或多个字母、数字或下划线。
string = "fix star and seven dog"

r1 = re.match(pattern, string)
if r1 is not None:
    print(f"r1: {r1.group()}")

r2 = re.search(pattern, string)
if r2 is not None:
    print(f"r2: {r2.group()}")

r3 = re.findall(pattern, string)
print(f"r3: {r3}")

# sub 将匹配到的数据进行替换
r4 = re.sub(pattern, "替换成这个词", string)
print(r4)

# split 根据匹配进行切割字符串，并返回一个列表
p = r"\|"
s = "x|y|z"
r5 = re.split(p, s)
print(r5)
