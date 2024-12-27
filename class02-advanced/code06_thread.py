from threading import Thread
import time


def funa(x, y):
    print(f"funa先执行{x}")
    time.sleep(2)
    print(f"funa再执行{y}")


class FooA(Thread):
    def run(self):
        print("执行FooA run开始")
        time.sleep(2)
        print("执行FooA run结束")


if __name__ == "__main__":
    t1 = Thread(target=funa, args=(1, 2), name="线程funa")
    t2 = FooA()
    t2.name = "线程FooA"
    # 设置守护线程
    # t1.setDaemon(True) #不推荐使用此方法了
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()

    # 如果没有join会发现有时候主线程执行完了，子线程部分语句还没执行
    # 加上join让主线程等待子线程执行完毕
    t1.join()
    t2.join()

    print(f"{t1.name} 执行结束")
    print(f"{t2.name} 执行结束")
    print(f"主线程执行结束")
