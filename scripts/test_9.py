"""
本代码用于Python的零基础学习
"""
import random

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 面向对象的编程 封装 继承 多态 类型注解 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ###
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 面向对象 ##############################################################################################################
# 面向对象的编程三大主要特征：封装，继承，多态
#   封装：将现实世界事物的属性和行为在类中描述为成员变量和成员方法
#       class 类名:
#           类内容体
#   继承：分为单继承和多继承，子类或派生类拥有父类或基类的所有公有成员或受保护成员，无法直接使用父类或基类的私有成员
#       class 类名(父类名1, 父类名2..):
#           新增类内容体或pass关键字
#       在多继承中，先继承的先保留，后继承的被覆盖，即左边父类优先
#       复写父类成员语法：在子类中重新定义同名的属性或方法即可，此时子类中的内容将覆盖父类中的内容
#       子类中调用父类成员：在复写后，如果想要调用已被复写的原来父类中的成员(只能在子类内调用，子类的实体类对象只能调用复写的)：
#           方法一：在子类中以“父类名.成员变量”或“父类名.成员方法(self)”调用
#           方法二：在子类中以“super.成员变量”或“super.成员方法()”调用
#   多态：同样的行为(函数)，传入不同的对象，得到不同的状态
#       多态常作用在继承关系上：以父类做定义声明，实际传入子类对象进行工作，从而实现获得同一行为，不同状态
#       抽象类(接口)：含有抽象方法的类称之为抽象类，用于父类来确定有哪些方法，而具体的方法实现是由子类自行决定的
#       抽象方法：方法体是空实现的(pass)称之为抽象方法
# 私有成员变量：变量名以__开头，类对象无法对其赋值，也无法获取值，但是可以被类内其他成员使用
# 私有成员方法：方法名以__开头，无法直接被类对象使用，但是可以被类内其他成员使用
# 受保护成员：以_开头，在语法可访问性与类的继承性上功能一致，只不过在编程习惯中，不推荐被类外部随意访问
# 类型注解：在代码中涉及数据交互的地方，提供数据类型的注解(显式的说明)，帮助IDE对代码进行类型推断，协助做代码提示
#   类型注解仅仅是提示性的，不是决定性的
#   变量的类型注解：变量:类型  或  变量:类型=xxx  或  在注释中进行注解：# type:类型
#       一般只在无法直接看出变量类型时才会添加变量的类型注解
#   函数(方法)形参列表和返回值的类型注解：
#       形参注解：def 函数(方法)名(形参名: 类型, 形参名: 类型...)
#       返回值注解：def 函数(方法)名(形参...) -> 返回值类型
#   Union类型注解：Union[类型, 类型, ...]，对变量和函数的形参及返回值都适用，使用前需要先导入from typing import Union
#-----------------------------------------------------------------------------------------------------------------------

# 定义一个带有私有成员变量与私有成员方法的类 --------------------------------------------------------------------------------
class Phone:
    __current_voltage = 2.0    # 当前手机运行电压
    __is_5g_enable = True

    def __keep_single_core(self):
        """
        私有成员方法，无法被类对象使用，只能在类内被调用
        :return:
        """
        print(f"当前手机运行电压为：{self.__current_voltage}，保持CPU以单核模式运行...")

    def call_by_5g(self):
        """
        类内成员可以调用私有成员变量和私有成员方法
        :return:
        """
        if self.__current_voltage >= 1:
            print("5g通话已开启！")
        else:
            self.__keep_single_core()
            print("5g通话开始失败！")

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启！")
            return True
        else:
            print("5g关闭，使用4g网络！")
            return False

    def call_check_5g(self):
        self.__check_5g()
        print("正在通话中...")
#-----------------------------------------------------------------------------------------------------------------------

# 以继承的方式定义一个类 --------------------------------------------------------------------------------------------------
class Phone2024:
    IMEI = None     # 序列号
    producer = None # 生产商
    __current_voltage = 1.0 # 手机运行电压

    def call_by_4g(self):
        print(f"{self.__current_voltage}，4g通话...")

    def return_current_vol(self):
        return self.__current_voltage

class Phone2025(Phone2024):
    face_id = None  # 新增面部识别功能
    IMEI = "9527"   # 复写父类成员变量

    def call_by_5g(self):   # 新增5g通话功能
        print(f"{self.return_current_vol()}，5g通话...")

    def call_by_4g(self):   # 复写父类成员方法
        print(f"现在是子类的call_by_4g函数")
#-----------------------------------------------------------------------------------------------------------------------

# 定义一个抽象类 ---------------------------------------------------------------------------------------------------------
class AC:
    """
    一个空调的抽象类
    """
    def cool_wind(self):
        """
        实现空调制冷功能
        :return:
        """
        pass

    def hot_wind(self):
        """
        实现空调制热功能
        :return:
        """
        pass

    def swing_l_r(self):
        """
        实现空调左右摆风功能
        :return:
        """
        pass
#-----------------------------------------------------------------------------------------------------------------------

# 基于抽象类实现多态 -----------------------------------------------------------------------------------------------------
class Medea_AC(AC):
    def cool_wind(self):
        print("medea空调制冷科技")

    def hot_wind(self):
        print("medea空调制热科技")

    def swing_l_r(self):
        print("medea空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("GREE空调制冷科技")

    def hot_wind(self):
        print("GREE空调制热科技")

    def swing_l_r(self):
        print("GREE空调左右摆风")

def make_cool(ac: AC):
    """
    多态实现制冷函数
    :param ac:
    :return:
    """
    ac.cool_wind()

def make_hot(ac:AC):
    """
    多态实现制热函数
    :param ac:
    :return:
    """
    ac.hot_wind()

def make_swing(ac:AC):
    """
    多态实现摆风函数
    :param ac:
    :return:
    """
    ac.swing_l_r()
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # 测试带有私有成员的类和对象
    phone = Phone()
    # print(phone.__current_voltage)  # 将报错，无法使用
    # phone.__keep_single_core()  # 将报错，无法调用
    phone.call_by_5g()          # 可以正常运行
    phone.call_check_5g()       # 可以正常运行

    # 测试继承
    phone_2025 = Phone2025()
    phone_2025.call_by_4g()     # 调用在子类内复写后的函数
    phone_2025.call_by_5g()

    # 类型注解
    # 基础数据类型注解
    var_1: int = 10
    var_2: str = "阿玮"
    var_3: bool = True
    # 类对象类型注解
    class Student:
        pass
    stu:Student = Student()
    # 基础容器类型注解
    my_list: list = [1, 2, 3]
    my_tuple: tuple = (1, 2, 3)
    my_dict: dict = {"name": "阿玮"}
    # 类型容器详细注解(需python3.9以上)
    # my_list_d: list[int] = [1, 2, 3]
    # my_tuple_d: tuple[int, str, bool] = (1, "阿玮", True)
    # my_dict_d: dict[str, int] = {"age": 23}
    # 在注释中进行类型注解
    var_4 = 100      # type: int
    var_5 = "hello"  # type: str
    var_6 = True     # type: bool
    # 函数类型注解
    def my_add(x: int, y: int):  # 对函数形参进行类型注解
        return x + y
    def my_func(data) -> list:  # 对函数返回值进行类型注解
        return data
    # Union联合类型注解(需python3.9以上)
    # from typing import Union
    # my_list_union: list[Union[int, str]] = [1, "阿玮"]
    # def func_union(data: Union[int, str]) -> Union[int, str]:
    #     return data

    # 多态
    media_ac = Medea_AC()
    gree_ac = GREE_AC()
    make_cool(media_ac)     # 将调用子类Media_AC中cool_wind()函数
    make_cool(gree_ac)      # 将调用子类GREE_AC中cool_wind()函数
    make_hot(media_ac)      # 将调用子类Media_AC中cool_wind()函数
    make_hot(gree_ac)       # 将调用子类GREE_AC中cool_wind()函数
    make_swing(media_ac)    # 将调用子类Media_AC中cool_wind()函数
    make_swing(gree_ac)     # 将调用子类GREE_AC中cool_wind()函数

