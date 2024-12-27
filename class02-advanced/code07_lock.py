from threading import Thread, Lock

a = 0
b = 10000000

local = Lock()


def sum1():
    local.acquire()
    global a
    for i in range(b):
        a += 1
    print("sum1计算结果：", a)
    local.release()


def sum2():
    local.acquire()
    global a
    for i in range(b):
        a += 1
    print("sum2计算结果：", a)
    local.release()


if __name__ == "__main__":
    t1 = Thread(target=sum1)
    t2 = Thread(target=sum2)
    t1.start()
    t2.start()
