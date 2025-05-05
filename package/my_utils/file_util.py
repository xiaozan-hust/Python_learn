"""
该模块属于my_utils工具包
该模块用于处理文件相关工具，包含文件打印函数和文件追加写入函数
"""

def print_file_info(file_name):
    """
    文件打印函数：接受传入文件的路径，打印文件的全部内容
    :param file_name: 文件路径
    :return: None
    """
    file = None
    try:
        file = open(file_name, "r", encoding="UTF-8")
        contents = file.read()
        print(f"文件中的全部内容为：\n{contents}")
    except Exception as e:
        print(f"读取文件出现异常，原因为：{e}")
    finally:
        if file:
            file.close()

def append_to_file(file_name, data):
    """
    文件追加写入函数：接受文件路径及传入数据，将数据追加写入到文件中
    :param file_name: 文件路径
    :param data: 追加数据
    :return: None
    """
    file = None
    try:
        file = open(file_name, "a", encoding="UTF-8")
        file.write("\n")
        file.write(data)
        print(f"已在：{file_name}中追加写入数据：{data}")
    except Exception as e:
        print(f"追加写入数据出现异常，原因为：{e}")
    finally:
        if file:
            file.close()

if __name__ == "__main__":
    file_path = "../file/test.txt"
    print_file_info(file_path)
    append_to_file(file_path, "测试追加一个数据")
