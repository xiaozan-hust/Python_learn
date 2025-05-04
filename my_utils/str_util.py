"""
该模块属于my_utils工具包
该模块用于处理字符串相关工具，包含字符串反转函数和字符串切片函数
"""

def str_reserve(s):
    """
    该函数为字符串反转函数：接受传入字符串，将字符串反转返回
    :param s: 待反转的字符串
    :return: 反转后的字符串
    """
    s_reserve = s[::-1]
    return s_reserve

def substr(s, x, y):
    """
    该函数为字符串切片函数：按照下标x和y，对字符串进行切片
    :param s: 待切片的字符串
    :param x: 切片起始下标
    :param y: 切片结束下标
    :return: 切片完成后的字符串
    """
    s_sub = s[x:y]
    return s_sub

if __name__ == "__main__":
    str_test = "华中科技大学"
    str_res = str_reserve(str_test)
    str_sub = substr(str_test, 2, 4)
    print(f"反转后的字符串为：{str_res} \n切片后的字符串为：{str_sub}")

