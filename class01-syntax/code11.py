# 0——x累加
def funa(x):
    if x == 0:
        return 0
    return funa(x - 1) + x


print(funa(3))

res = funa  # 函数引用，就相当于给funa起了个别名
print(res(3))


# 装饰器模板
def logger(func):
    def wrapper(*args):
        print(f"开始执行函数 {func.__name__}")
        return func(*args)

    print(f"函数 {func.__name__} 执行完毕")
    return wrapper  # 装饰器必须返回内部方法名


@logger
def add(x, y):
    return x + y


@logger
def printm(x, y, z):
    print(x, y, z)


print(add(10, 20))
printm(1, 2, 3)

# fn = logger(add)
# print(fn(200, 100))  # 300

# 回调函数
call = lambda: print("call")


def funx(fun, *args):
    print(f"处理逻辑 {args}")
    # 处理完毕调用回调函数
    fun()


funx(call)
