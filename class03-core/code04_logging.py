import logging

logger = logging.getLogger()
# 设置级别
logger.setLevel(logging.DEBUG)

# 在控制台输出
sh = logging.StreamHandler()
# 控制台输出级别
sh.setLevel(logging.DEBUG)

# 写入文件中
fh = logging.FileHandler(r"D:\appCache\python\log\log.log", encoding="utf-8")
# 文件输出级别
fh.setLevel(logging.INFO)

# 日志输出格式
format = "%(asctime)s|%(levelname)s|%(filename)s|%(module)s|%(funcName)s|第%(lineno)d行|%(message)s"
formatter = logging.Formatter(format)
sh.setFormatter(formatter)
fh.setFormatter(formatter)

# 将sh和fh添加到logger handler中
logger.addHandler(sh)
logger.addHandler(fh)

# 测试
# logging.debug("""
# 这是中文，中国文字
# 啦啦啦啦啦
# this is debug
# """)
# logging.info("""
# 中文有没有问题
# this is info
# """)
# logging.error("this is error")
