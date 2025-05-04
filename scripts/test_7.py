"""
本代码用于Python的零基础学习
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 异常-模块-包综合案例 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 案例要求 ##############################################################################################################
# 创建一个自定义包，名称为：my_utils
# 在包内提供2个模块：
#       str_util.py(字符串相关工具，内含：)
#           函数：str_reverse(s)，接受传入字符串，将字符串反转返回
#           函数：substr(s, x, y)，按照下标x和y，对字符串进行切片
#       file_util.py(文件处理香瓜工具，内含：)
#           函数：print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
#           函数：append_to_file(file_name, data)，接收文件路径以及传入数据，将数据追加写入到文件中
#-----------------------------------------------------------------------------------------------------------------------

from my_utils import file_util
from my_utils.str_util import *
import my_utils.str_util

# 字符串功能测试
str_test = "华中科技大学"
print(f"字符串反转工具测试：{my_utils.str_util.str_reserve(str_test)}")
print(f"字符串切片工具测试：{substr(str_test, 2, 4)}")

# 文件功能测试
file_path = "../file/test.txt"
a_data = "测试追加数据"
print(f"文件打印工具测试：{file_util.print_file_info(file_path)}")
print(f"文件追加工具测试：{file_util.append_to_file(file_path, a_data)}")
