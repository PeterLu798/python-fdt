# 读文件
# f1 = open("Test.txt", "rb")
# try:
#     txt = f1.read()
#     print(txt.decode("utf-8"))
# finally:
#     f1.close()
# print("*" * 50)
# # 绝对路径
# f2 = open(r"D:\Foo.txt", "rb")  # windows下用r转义
# try:
#     content = f2.read()
#     print(content.decode("utf-8"))
# finally:
#     f2.close()

# 写文件
# 以二进制覆盖写
# f3 = open("Foo.txt", "wb")
# try:
#     content = """
#     这是中文，
#     This is English
#     """
#     f3.write(content.encode(encoding="utf-8"))
# finally:
#     f3.close()

# # 以二进制追加写
# f3 = open("Foo.txt", "ab")
# try:
#     content = "追加一段文字\n"
#     f3.write(content.encode(encoding="utf-8"))
# finally:
#     f3.close()

# print("*" * 50)
# # 以二进制读出来
# f4 = open("Foo.txt", "rb")
# try:
#     print(f4.read().decode(encoding="utf-8"))
# finally:
#     f4.close()

# # with的作用相当于try...finally，只不过将finally中的close自动执行了
# with open("Foo.txt", "rb") as f5:
#     print(f5.read().decode(encoding="utf-8"))
#
# # 查看f5的关闭状态
# print(f5.closed)  # True

# # tell方法和seek方法
# with open("Foo.txt", "rb") as f:
#     print(f.read(12).decode(encoding="utf-8"))  # 注意这里一个汉字4字节
#     print(f.tell())  # tell方法返回当前指针所在位置 12
#
#     f.seek(0, 0)  # 第一个0是偏移量，第二个0是指针指向的开始位置
#     print(f.tell())  # 0

# 文件备份
class CopyFile:
    @staticmethod
    def copy(filepath):
        index = filepath.rfind(".")
        new_file_path = None
        if index == -1:
            new_file_path = filepath + "(备份)"
        else:
            new_file_path = filepath[:index] + "(备份)" + filepath[index:]
        print(new_file_path)
        f1 = open(filepath, "rb")
        f2 = open(new_file_path, "wb")
        try:
            while True:
                content = f1.read(1024)
                if len(content) == 0:
                    break
                f2.write(content)
        finally:
            f1.close()
            f2.close()


# # 目录操作
# import os
#
# # 文件（夹）重命名
# os.rename("Foo2.txt", "Foo2.txt")
# # 创建文件夹
# os.mkdir("D:/wilia")  # 只能创建一层
# # 删除文件
# os.remove("D:/wilia")
# # 获取当前目录
# print(os.getcwd())
# # 改变默认路径
# os.chdir("../")
# # 获取目录列表
# print(os.listdir())

with open("Foo2.txt", encoding="utf-8") as f:
    while True:
        txt = f.readline()
        if not txt:
            break
        print(txt, end="")

with open("Foo2.txt", encoding="utf-8") as f:
    print(f.readlines())  # ['追加一段文字\n', '追加一段文字\n', '追加一段文字\n', '追加一段文字\n', '追加一段文字\n']
