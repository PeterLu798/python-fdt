from greenlet import greenlet
import gevent, time
from gevent import monkey

# def process():
#     print(f"save user")
#     # 切换到g2协程中执行process2
#     g2.switch("pdf", "word")
#     print(f"save order")
#
#
# def process2(a, b):
#     print(f"read {a}")
#     print(f"read {b}")
#     # 执行完process2后继续切回g1执行process
#     g1.switch()
#
#
# g1 = greenlet(process)
# g2 = greenlet(process2)
#
# # 先执行g1
# g1.switch()


# def funa(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#         # sleep用来模拟一个耗时操作，注意要用gevent的sleep
#         gevent.sleep(1)
#
#
# g3 = gevent.spawn(funa, 2)
# g4 = gevent.spawn(funa, 2)
# g5 = gevent.spawn(funa, 2)
#
# g3.join()

"""
********patch_all演示开始**************
"""
# monkey.patch_all()
#
#
# def funa(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#         # 因为前面申明了monkey.patch_all()，所以这里的time.sleep方法被自动替换成了gevent下非阻塞的同名实现函数
#         time.sleep(1)
#
#
# g3 = gevent.spawn(funa, 2)
# g4 = gevent.spawn(funa, 2)
# g5 = gevent.spawn(funa, 2)
#
# g3.join()
# print("这句话啥时候执行")
"""
********patch_all演示开始**************
"""
"""
********joinall演示开始**************
"""


def func1():
    print('func1开始运行！')
    gevent.sleep(0.3)
    print('func1继续运行。')


def func2():
    print('func2开始运行！')
    gevent.sleep(0.2)
    print('func2继续运行。')


def func3():
    print('func3开始运行！')
    gevent.sleep(0.1)
    print('func3继续运行。')


gevent.joinall((
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
))
"""
********joinall演示结束**************
"""
