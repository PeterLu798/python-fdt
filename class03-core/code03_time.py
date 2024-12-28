import code04_logging
import time

logger = code04_logging.logger

print(time.time())  # 时间戳，1970年1月1日0时到现在的秒数

t = time.localtime()
print(t)  # time.struct_time(tm_year=2024, tm_mon=12, tm_mday=28, tm_hour=15, tm_min=46, tm_sec=5,
# tm_wday=5, tm_yday=363, tm_isdst=0)
print(t.tm_year)  # 2024
print(t[0])  # 2024

# localtime和时间戳之间的转换
## 时间戳转localtime
print(time.localtime(time.time()))
## localtime转时间戳
print(time.mktime(t))

print(time.asctime())  # Sat Dec 28 15:48:47 2024

# localtime格式化输出
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 2024-12-28 15:52:35

# 格式化时间转localtime
str = "2024-12-28 15:52:35"
print(time.strptime(str, "%Y-%m-%d %H:%M:%S"))

logger.info("这里能不能打日志")
