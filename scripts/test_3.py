"""
本代码用于Python的零基础学习
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  函数定义 函数嵌套 函数功能说明 global关键字 多返回值函数 多种参数传递 匿名函数 # # # # # # # # # # # ###
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 函数：组织好的，可重复使用的，用来实现特定功能的代码段 ######################################################################
#-----------------------------------------------------------------------------------------------------------------------
# def 函数名(形参1, 形参2...):
#     """
#     函数功能说明
#     :param x:*******
#     :param y:********
#     :return:*******
#     """
#     函数体
#     return 返回值或None
# 使用方法：函数名(实参) 或 变量 = 函数名(实参)
#-----------------------------------------------------------------------------------------------------------------------
# 其中参数与返回值不是必须的
# 遇到return或缩进后函数执行结束
# 若函数无返回值，其实函数会返回None，依然可以用变量去接收它
# 即使有返回值也不一定必须要用变量去接收它
# 编写函数说明文档后，鼠标悬停在函数处，可以显示函数使用方法
# 函数可以嵌套调用

# 书写一个“标准”的函数
def my_len(str_):
    """
    my_len()函数用于输出字符串长度
    :param str_:
    :return:
    """
    count = 0
    for i in str_:
        count += 1
    return count
name_1 = "450315c"
name_2 = "hdshds"
my_len(name_1)              # 即使有返回值也不一定必须要用变量去接收它
print(my_len(name_1), my_len(name_2))

# 返回值可以是None，可以用作逻辑中
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result = check_age(10)
if result:
    print("你已成年")
else:
    print("你未成年")

# 函数支持多个返回值
def test_return():
    return 1, True, "Hello"
x, y, z = test_return()
print(x, y, z)

# 局部变量：在函数体内部定义，函数调用结束后，销毁局部变量
# 全局变量：在函数体内，外皆可使用的变量
# global关键字：如果要在函数体内容对变量进行修改，可以在函数内部声明变量为全局变量
test_num = 100
def print_test_num_a():
    test_num = 200          # 此处相当于又新定义了一个test_num，所以不会修改外部的test_num的值
    print(f"{test_num}")    # 打印200

def print_test_num_b():
    global test_num         # 设置test_num为全局变量，即此处的test_num为外部定义的那个test_num
    test_num = 200
    print(f"{test_num}")    # 打印200

print_test_num_a()
print(f"{test_num}")        # 还是打印100
print_test_num_b()
print(f"{test_num}")        # 变为打印200

# 函数综合案例 ##########################################################################################################
all_money = 5000000
name = None
name = input("请输入你的名字(小心点，我知道你叫阿玮)：")   # 若不使用某个变量而直接对其修改，那么会报这个警告
def print_menu():
    print("------------主菜单------------")
    print(f"{name}，你好，欢迎来到尖沙咀银行ATM，请选择操作：")
    print("查询余额 [输入1] \n存款 \t[输入2] \n取款 \t[输入3] \n退出 \t[输入4]")
def print_money():
    print(f"{name}，你好，你的余额剩余：{all_money}元")
def save_money(money_):
    global all_money
    all_money += money_                             # 不能直接使用all_money，必须要先使用global关键字声明一下
    print(f"{name}，你好，你成功存款{money_}元，账户余额剩余：{all_money}元")
def draw_money(money_):
    global all_money
    all_money -= money_
    print(f"{name}，你好，你成功取款{money_}元，账户余额剩余：{all_money}元")
while True:
    print_menu()
    choice = int(input("请输入你的选择："))
    if choice == 1:
        print_money()
    elif choice == 2:
        temp_money = int(input("请输入存款金额(元)："))
        save_money(temp_money)
    elif choice == 3:
        temp_money = int(input("请输入取款金额(元)："))
        if all_money >= temp_money:
            draw_money(temp_money)
        else:
            print(f"余额不足，账户余额剩余{all_money}元")
    elif choice == 4:
        break
    else:
        print("你输入的数字有误，请重新输入！")

# 函数的进阶用法 #########################################################################################################
# 函数可以有多个返回值：如return 1, 2     调用时：x, y = 函数()
# 函数的参数调用：
#   位置参数：调用函数时根据函数定义的参数位置来传递参数
#   关键字参数：调用函数时通过“键=值”的形式传递参数，还可以和位置参数混合使用，但是此时必须位置参数在前，且与参数顺序对应
#   缺省参数(默认参数)：调用函数时可以不传该默认参数的值，函数将使用默认值；若传，则修改默认参数值。所有位置参数必须出现在默认参数前，包括函数定义和调用
#   不定长参数(可变参数)：用于不确定调用的时候会传递多少个参数(不传参也可以)的场景，分为位置传递和关键字传递
# python中函数不支持函数重载，即若定义多个同名函数，按照执行顺序，相当于是会重新定义
# 函数作为参数传递：分为函数作为参数传递与lambda匿名函数两种方式
#  ---------------------------------------------------------------------------------------------------------------------
# 定义一个函数
def user_info(user_name, age, gender, school="华中科技大学"):
    print(f"你的名字是: {user_name}, 年龄是: {age}, 性别是: {gender}, 学校为: {school}")
# 位置调用
user_info("阿玮", 22, "男")
# 关键字调用
user_info(user_name="阿玮", age=22, gender="男")   # 不必按照固定顺序
user_info(age=22, user_name="阿玮", gender="男")   # 不必按照固定顺序
user_info("阿玮", age=22, gender="男")   # 可以与位置参数混合使用
# 缺省参数
user_info(user_name="阿玮", age=22, gender="男", school="耶鲁大学")

# 不定长参数-位置传递：所有传进的参数会根据位置被合并为一个元组 ----------------------------------------------------------------
def user_info(*args):
    print(args)
# 位置调用
user_info("阿玮", 19, "耶鲁大学")
# 不定长参数-关键字传递：“键=值”方式传递，将会根据“key=value”形成字典
def user_info(**kwargs):
    print(kwargs)
# 关键字调用
user_info(user_name = "阿玮", age=22, gender="男")

# 函数作为参数传递：数据确定，逻辑不确定，如下的例子，确定的是对1和2进行操作，但是至于是相加还是相乘，就看你使用哪个函数作为参数了
# 前面讲的函数的例子都是逻辑确定，数据不确定；当逻辑不确定但是数据确定时可以考虑将函数作为参数传递 ---------------------------------
def test_func(compute_func):
    result_ = compute_func(1, 2)
    print(result_)
# 传递函数为参数: 先定义一个函数，然后将该函数作为参数传递给test_func
def compute_add(x_, y_):
    return x_ + y_
def compute_mul(x_, y_):
    return x_ * y_
test_func(compute_add)
test_func(compute_mul)

# lambda匿名函数 --------------------------------------------------------------------------------------------------------
# lambda 传入参数：函数体(只能一行代码)
# lambda相当于是定义了一个无名称的函数，只可临时使用一次；对比之下，非匿名函数(即有名称的函数)，可以基于名称重复使用
# 如果要写多行代码时，应使用def定义带名函数
# 以上面的代码为例，其实可以不用显示定义compute函数，而采用lambda的形式：
test_func(lambda x_, y_: x_ + y_)
test_func(lambda x_, y_: x_ * y_)

