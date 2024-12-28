import os

# 读取环境变量
print(os.getenv("path"))

print(os.path.split(r"D:\test.py"))  # ('D:\\', 'test.py')
print(os.path.dirname(r"D:\test.py"))  # D:\
print(os.path.basename(r"D:\test.py"))  # test.py

print(os.path.exists(r"D:\test.py"))  # False
print(os.path.isfile(r"D:\Foo.txt"))  # True
print(os.path.isdir(r"D:\git"))  # True

print(os.path.abspath("."))  # 当前路径的绝对路径
print(os.path.abspath("../"))  # 上层目录的绝对路径
