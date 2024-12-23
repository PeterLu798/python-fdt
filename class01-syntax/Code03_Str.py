# encode编码
str1 = "hello world"
stream = str1.encode("utf-8")  # 默认utf-8
print(type(stream))  # <class 'bytes'>

# b
s1 = b"hello"
print(type(s1))  # <class 'bytes'>

# decode解码
s2 = b"hha"
print(s2.decode("utf-8"))

# 索引
s3 = "abcd"
print(s3[0])
print(s3[3])
print(s3[-1])
print(s3[-2])

# 字符串的切片
name = "class_name_peter"
print(name[6:10:1])  # name
print(name[6:10:2])  # nm
print(name[:])  # class_name_peter
print(name[-1:3:-1])  # retep_eman_s

# find
mytest = "this is my test"
print(mytest.find("this"))  # 0
print(mytest.find("hello"))  # -1
# index
print(mytest.index("this"))
# print(mytest.index("hello")) # ValueError: substring not found
# count
print(mytest.count("t"))  # 3
print(mytest.count("hello"))  # 0

# replace
test1 = "this is test1"
print(test1.replace("t", "T"))  # This is TesT1
print(test1.replace("t", "T", 1))  # This is test1

# split
test2 = "what a fuck this world"
print(test2.split(" "))  # ['what', 'a', 'fuck', 'this', 'world']
print(test2.split(" ", 1))  # ['what', 'a fuck this world']

# capitalize
print(test1.capitalize())  # This is test1

# lower
test3 = "HELLO WORLD"
print(test3.lower())  # hello world
# upper
test4 = "how are you"
print(test4.upper())  # HOW ARE YOU
# title
print(test4.title())  # How Are You
# islower
print(test4.islower())
test5 = "How are you"
print(test5.islower())
# isupper
print(test5.isupper())
print(test3.isupper())

# isdigit
numStr = "124"
print(numStr.isdigit())  # True
strNum = "3.1E5"
print(strNum.isdigit())  # False

# startswith
print(test5.startswith("how"))  # False
print(test5.startswith("How"))  # True
# endswith
print(test5.endswith("you"))

# join
code = "python"
print("*".join(code))  # p*y*t*h*o*n

#
desc = "   这是一段化    反转反对反对的，what is   this?   dd ??  "
print(desc.strip())
print(desc.lstrip())
print(desc.rstrip())
