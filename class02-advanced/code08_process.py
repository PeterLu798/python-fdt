from multiprocessing import Process, Queue
import os


def exe1():
    print(f"exe1 进程Id为{os.getpid()}, 父进程Id为{os.getppid()}")


def exe2():
    print(f"exe2 进程Id为{os.getpid()} 父进程Id为{os.getppid()}")


# if __name__ == "__main__":
#     p1 = Process(target=exe1, name="进程exe1")
#     p2 = Process(target=exe2, name="进程exe2")
#     p1.start()
#     p2.start()
#     print(f"主进程Id为{os.getpid()}, 主进程ppid为{os.getppid()}")

list1 = []


def listadd():
    for i in range(10):
        list1.append(i)
    print(list1)


def listprint():
    print(list1)


# if __name__ == "__main__":
#     p1 = Process(target=listadd)
#     p2 = Process(target=listprint)
#     p1.start()
#     p1.join()
#     p2.start()

# q = Queue(3)  # 队列：先进先出
# q.put("消息1")  # put用来往队列放数据
# q.put("消息2")
# print(q.full())  # full判断队列是否满了
# q.put("消息3")
# print(q.full())
#
# print(q.get())  # get用来取出队列中的数据
# print(q.get())
# print(q.get())
# print(q.empty())  # empty判断队列是否为空
# print(q.qsize())  # qsize 返回队列当前大小

# 使用队列进行进程间通信
def write(queue, list):
    for i in list:
        if not queue.full():
            queue.put(i)
        else:
            raise Exception("队列已满")


def read(queue):
    while not queue.empty():
        print(queue.get())


if __name__ == "__main__":
    queue = Queue(100)
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    p1 = Process(target=write, args=(queue, li))
    p2 = Process(target=read, args=(queue,))
    p1.start()
    p1.join()  # 如果这里不等待p1执行完毕，有时候p2先执行会读不到数据
    p2.start()

