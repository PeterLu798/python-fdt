from multiprocessing import Pool, Manager
import time


def square(x):
    time.sleep(2)  # 加sleep主要是为了看执行时间
    return x * x


if __name__ == "__main__":
    s1 = time.time()
    p = Pool(4)
    li = []
    for i in range(6):
        result = p.apply_async(square, args=(
            i,))  # result返回的对象是 <multiprocessing.pool.ApplyResult object at 0x000002779316E780>
        li.append(result)
    # 关闭进程池，关闭之后p不再接受新的请求
    p.close()
    # join方法等待上面计算完毕
    p.join()
    for j in li:
        print(j.get())  # 要想拿到真正的返回数据，必须调用get()方法
    print(f"异步执行时间 {time.time() - s1} 秒")  # 异步执行时间 4.067576885223389 秒

if __name__ == "__main__":
    s2 = time.time()
    p = Pool(4)
    li = []
    for i in range(6):
        result = p.apply(square, args=(i,))  # 同步执行返回的就是真正的数据
        li.append(result)
    # 关闭进程池，关闭之后p不再接受新的请求
    p.close()
    # join方法等待上面计算完毕
    p.join()
    print(li)
    print(f"同步执行时间 {time.time() - s2} 秒")  # 同步执行时间 12.062416315078735 秒
