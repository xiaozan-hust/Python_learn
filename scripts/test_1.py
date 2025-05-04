"""
本代码用于Python的零基础学习
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 注释 变量 数据类型 数据类型转换 标识符 运算符 字符串的拼接、格式化 print()函数的使用 input()函数的使用 ####
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# print()函数
# print(内容, end='')即可输出不换行
print(1234)
print("hello world")
print("中文测试")
money = 50
money = money - 10
print("钱包剩余：", money, "元。")

# type()函数：查看数据类型
data_type = type(money)
print(data_type)
print(type(money))

# 数据类型转换
money_int = int(money)
money_float = float(money)
money_str = str(money)
print("money_int: ", type(money_int), "; money_float: ", type(money_float), "; money_str: ", type(money_str))

# 运算符：加(+); 减(-); 乘(*); 除(/) 取整除(//); 取余(%); 指数(**)
# 复合运算符：+=；-=；*=；/=；%=；**=；//=

# 字符串定义方式：单引号'xxx'，双引号"xxx"，三引号'''xxx'''
# 转义字符: \  用于解除后面的引号的作用
name = "\"例程来自黑马程序员\""
print(name)

# 字符串拼接
str_1 = "我今年"
age = 24
print(str_1 + str(age))     # 不能进行字符串与其他类型变量的直接拼接，需要进行数据转换str()函数
# 字符串拼接：占位拼接方式: %表示占位，s表示将变量转换成字符串放到占位的位置
# %s: 转换成字符串类型后占位   %d: 转换成整数类型后占位   %f: 转换成浮点数类型后占位
salary = 16789
str_2 = "黑马程序员"
str_3 = "毕业平均工资"
print("%s" %str_3)
print("毕业平均工资 %s" %salary)
print("毕业平均工资 %s %s" % (salary, salary))
print("毕业平均工资 %s" % str_2)

# 字符串精度控制
# %5d：表示将整数的宽度设置为5，如数字11，输出将为：空格空格空格11
# %7.2f：表示宽度设置为7，小数点精度设置为2，如数字11.345，输出将为：空格空格11.35（其中小数部分被四舍五入）
# %.2f：表示不限制宽度，只设置小数点精度为2，如数字11.345，输出将为：11.35
num1 = 11
num2 = 11.345
print("宽度设置为5 %5d" %num1)
print("宽度设置为7，小数点精度设置为2 %7.2f" %num2)
print("不限制宽度，只设置小数点精度为2 %.2f" %num2)

# 字符串格式化
# f"内容{变量}"：该方法更为快捷，适用于任何类型变量，但是无法做精度控制，其中f指的是format
print(f"我今年{num1}, 我是{num2}")
print(f"{num1} {num2}")

# 表达式格式化
# 以上的字符串都是对变量进行的，其实也可以直接对表达式使用，比如a=2*3，其中a属于变量，2*3就属于表达式
print("1*1的结果是：%d" %(1*1))
print("字符串在python中的类型名为：%s" % type("字符串"))
print("字符串在python中的类型名为：%s" % "字符串")
print(f"1*2的结果是{1*2}")

# input() 输入后将内容存储为字符串类型的变量
print("告诉我你的名字：")
name = input()
print("Get!! 你是：%s" %name)
name = input("告诉我你的名字：")
print("Get!! 你是：%s" %name)