"""
本代码用于Python的零基础学习
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    # # # # # # # # # # # # # # # # # # #  ###
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 异常 #################################################################################################################
# 即BUG，程序执行到该处时将无法继续执行
# 捕获异常：提前假设某处会出现异常，做好提前准备，当真的出现异常时，有对应的后续手段
#     捕获常规异常语法：try: 可能发生异常的代码 except: 如果出现异常执行的代码(或者 except Exception as xx)
#     捕获指定异常语法：try: 可能发生异常的代码 except 报错类型 as xx: 如果出现异常执行的代码
#     捕获多个异常语法：try: 可能发生异常的代码 except (报错类型1, 报错类型2): 如果出现异常执行的代码
# 异常else：else后为没有异常时要执行的代码
#     语法为 try: 可能发生的异常 except: 如果异常执行的代码 else: 如果没有异常执行的代码
# 异常finally：finally后为无论是否异常都要执行的代码
#     语法为 try: 可能发生的异常 except: 如果异常执行的代码 else: 如果没有异常执行的代码 finally: 最后总要执行的代码
# 异常具有传递性
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# 捕获常规异常(捕获全部异常)
try:
    file = open("../file/test.txt", "r", encoding="UTF-8")
# except:
except Exception as e:
    print("目标文件不存在，创建新文件...")
    file = open("../file/test.txt", "w", encoding="UTF-8")
# 捕获指定异常
try:
    print(1/0)
except ZeroDivisionError as e:
    print("公式错误！")
    print(e)
try:
    print(name)
except NameError as e:
    print("未定义变量name！")
    print(e)
# 捕获多个异常
try:
    print(1/0)
    print(name)
except (ZeroDivisionError, NameError) as e:
    print("公式错误或未定义变量name!")
    print(e)
# 异常else
try:
    print("name")
except Exception as e:
    print("出现了异常！", e)
else:
    print("没有出现异常！")
# 异常finally
try:
    print(1 / 0)
except Exception as e:
    print(e)
finally:
    print("程序结束！")

# Module(模块) #########################################################################################################
# 模块是一个.py文件，里面可以定义类，函数，变量，可执行代码等，可以导入模块进行使用
# 语法：[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]    其中*表示全部，[]表示可选，只有import是必须的
# 自定义模块：自行编写一个python文件，文件名即模块名，文件名需符合标识符命名规则，可以按照上述方式进行导入使用
#       导入该程序下某文件夹下的某模块：from 文件夹.文件名 import 内容(或者import 文件夹.文件名)
#       导入该程序同级文件夹下的某模块：from 文件名 import 内容(或者import 文件名)
#       导入该程序上级文件夹下的某模块：
#           import os, sys
#           parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 获取上一级目录的绝对路径
#           other_dir = os.path.join(parent_dir, 'other_dir')                        # 构建 other_dir 的绝对路径
#           sys.path.append(other_dir)                                               # 将 other_dir 添加到系统路径中
#           from 文件名 import 内容(或者import 文件名)
# 当导入多个模块的时候，且模块内有同名功能，当调用这个同名功能时，实际调用到的是后面导入的模块的功能
# __main__：只有在运行该程序时，python中的内置变量__name__会变成__main__，此时当有其他程序调用该模块时，并不会触发这个条件
# __all__：一般写在文件最前面，定义该变量后，其他程序使用import *时，只能导入这个__all__列表内的元素，例如__all__ = ['test_A'] (但是可以手动导入，如import test_B)
#-----------------------------------------------------------------------------------------------------------------------
import time
time.sleep(1)   # 此时可以通过"模块."调用模块内各种函数，变量等
from time import sleep
sleep(1)        # 此时可以直接使用该函数(变量同理)
from time import *
sleep(1)        # 此时可以直接使用该模块内所有内容
import time as tt
tt.sleep(1)     # 此时可以使用别名调用该模块内所有内容
from time import sleep as tt
tt(1)           # 此时可以使用别名使用该函数
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# 该方式只在运行该程序时为true，故可以在后面写一些调试程序
# 但是直接写的程序，比如上面的try内容，依然会在import时或执行程序时被运行
if __name__ == "__main__":
    print("使用__main__去调试程序")
#-----------------------------------------------------------------------------------------------------------------------

# Package(包) ##########################################################################################################
# 概念：实体为包含了多个python文件(模块)和__init__.py文件的文件夹，包名即文件夹名，用于解决python的模块太多而可能造成的混乱
# 是__init__.py文件的存在，将一个普通的文件夹被标记成了Package，_init_.py文件可以在pycharm中自动创建，也可以手动创建，内容可以为空
# 导入方式：
#     方式一：导入：import 包名.模块名(或from 包名 import 模块名等等)  ;  使用：包名.模块名.目标
#     方式二：在__init__.py文件中添加__all__=[模块的名字, 模块的名字]，可以控制import * 导入的模块列表(可以手动import未导入的模块)
#-----------------------------------------------------------------------------------------------------------------------



