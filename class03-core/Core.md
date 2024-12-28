# 语法核心
## os模块
### [code01_os.py](code01_os.py)
## sys模块
### [code02_sys.py](code02_sys.py)
## time模块
### [code03_time.py](code03_time.py)
## logging模块
### [code04_logging.py](code04_logging.py)
1. 定义全局logger：[code04_logging.py](code04_logging.py)
2. 在别的文件中引用该模块并使用logger
````python
import code04_logging

logger = code04_logging.logger
logger.info("这里能不能打日志")
````