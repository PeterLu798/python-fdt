# 查看内置模块
import builtins

# print(dir(builtins))

# 安装第三方模块
from pdfminer.high_level import extract_pages

# 自定义模块
from tools import Timetools as timetools

print(timetools.now())
print(timetools.my_time_zone)
