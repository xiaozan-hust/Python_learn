"""
本代码用于Python的零基础学习
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 类和对象 构造方法 魔术方法 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ###
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 类和对象 ##############################################################################################################
# 定义：
#   class 类名称:
#       类的属性：定义在类中的变量(成员变量)
#       类的行为：定义在类中的函数(成员方法)
# 创建类对象：对象名 = 类名称() (若有参数可传参)
# 类的行为定义规则：
#   def 方法名(self, 形参1, 形参2, ... ):
#       方法体
#   self关键字必须存在，用于表示类对象自身的意思
#   当使用类对象调用方法时，self会被自动传入，我们无需理会
#   在方法内部，想要访问类的成员变量，必须使用self
# 面向对象编程：基于类创建对象，然后用对象来完成具体的工作。可以理解为类是一种“设计图纸”，而对象是基于图纸生产的“具体实体”
# 构造函数：__init__()
#   在创建类对象时会自动执行，将传入参数自动传递给__init__()方法使用
#   此时其实可以不单独写类的变量，在__init__()的方法体中使用了哪些变量即会在类内自动定义那些变量，如果单独写出，相当于是在该方法内进行赋值
# 其他魔术方法(构造函数也属于)：内置的类方法，可以实现各自特殊的功能，类似于C++中的运算符重载，使类对象具备类似列表或元组的一些效果
#   __str__：控制类转换成字符串的行为或者说print的行为，必须要有return，执行print(类对象)其实就是在调用该函数
#   __lt__：自行定义实现类对象大于或小于的功能比较，return为True或False，执行类对象>类对象(或类对象<类对象)其实就是在调用该函数
#   __le__：自行定义实现类对象大于等于或小于等于的功能比较，return为True或False，执行类对象>=类对象(或类对象<=类对象)其实就是在调用该函数
#   __eq__：自行定义实现类对象等于的功能判断，return为True或False，执行类对象==类对象其实就是在调用该函数
#   __call__：自行定义实现类对象类似函数一样被调用的功能，return可有可无，执行类对象()其实就是在调用该函数
# 私有成员(具体见test_9.py)
#-----------------------------------------------------------------------------------------------------------------------

# 定义一个简单的类为例 ---------------------------------------------------------------------------------------------------
class Student:
    name = None

    def say_hi_1(self):
        print(f"大家好，我的名字是{self.name}")

    def say_hi_2(self, msg):
        print(f"大家好，我的名字是{self.name}，{msg}")

# 定义一个带有构造方法的类 ------------------------------------------------------------------------------------------------
class Clock:
    # id = None       # 在__init__()存在下，此处可省略
    # price = None    # 在__init__()存在下，此处可省略

    def __init__(self, id_, price_):
        self.id = id_
        self.price = price_
        print("Clock类创建了一个类对象")

    def print_data(self):
        print(f"这个闹钟的编号为：{self.id}，购买价格为：{self.price}")

# 定义另一个带有构造方法的类 ----------------------------------------------------------------------------------------------
class Teacher:
    def __init__(self):
        self.name = input("请输入老师姓名：")
        self.age = input("请输入老师年龄：")
        self.address = input("请输入老师地址：")

    def print_data(self):
        print(f"老师姓名：{self.name}；老师年龄：{self.age}；老师住址：{self.address}")

# 定义一个使用魔术方法的类 ------------------------------------------------------------------------------------------------
class MagicName:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """
        若无该方法，类对象需要被转换成字符串时会输出内存地址，该方法的存在可以控制类转换成字符串的行为或者说print的行为
        :return: 自行定义
        """
        return f"类对象：name={self.name}，age={self.age}"

    def __lt__(self, other):
        """
        若无该方法，比较类对象时将会报错，该方法的存在可以自行定义实现类对象大于或小于的功能比较
        :param other: 另一个类对象
        :return: True或False
        """
        return self.age < other.age

    def __le__(self, other):
        """
        若无该方法，比较类对象时将会报错，该方法的存在可以自行定义实现类对象大于等于或小于等于的功能比较
        :param other: 另一个类对象
        :return: True或False
        """
        return self.age <= other.age

    def __eq__(self, other):
        """
        若无该方法，比较类对象时将会报错，该方法的存在可以自行定义实现类对象等于的功能判断
        :param other: 另一个类对象
        :return: True或False
        """
        return self.age == other.age

if __name__ == "__main__":
    # 测试类和对象
    stu_1 = Student()
    stu_2 = Student()
    stu_1.name = "阿玮"
    stu_2.name = "卤蛋"
    stu_1.say_hi_1()
    stu_2.say_hi_2("我想考公了~~")

    # 测试带有构造函数的类和对象
    clock_1 = Clock("9527", 19.99)
    clock_1.print_data()

    # 测试带有构造函数的类和对象
    teacher_num = int(input("请输入待记录老师人数："))
    teacher_data = list()
    for i in range(teacher_num):
        print(f"当前录入第{i}位老师的信息，总共需录入{teacher_num}位老师的信息")
        tea = Teacher()
        tea_temp = dict()
        tea_temp["老师姓名"] = tea.name
        tea_temp["老师年龄"] = tea.age
        tea_temp["老师地址"] = tea.address
        teacher_data.append(tea_temp)
        print(f"老师{i}信息录入完成，相关信息为：")
        tea.print_data()
    print(f"全部信息录入完成，信息总表如下：{teacher_data}")

    # 测试带有魔术方法的类和对象
    mag_1 = MagicName("阿玮", 23)
    mag_2 = MagicName("卤蛋", 24)
    print(mag_1)            # 测试__str__
    print(str(mag_1))
    print(mag_1 < mag_2)    # 测试__lt__
    print(mag_1 <= mag_2)   # 测试__le__
    print(mag_1 == mag_2)   # 测试__eq__

