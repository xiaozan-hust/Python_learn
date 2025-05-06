"""
和文件相关的类定义
"""
import json
from typing import List
from package.data_anysis.data_define import Record


class FileReader:

    def __init__(self, path):
        """
        记录待读取文件路径
        :param path: 文件路径
        """
        self.path = path

    def read_data(self) -> List[Record]:
        """
        读取文件的数据，将每一条数据都转换成Record对象，将它们都封装到list内返回
        """
        pass

class TextFileReader(FileReader):

    def read_data(self) -> List[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        lines = f.readlines()
        records = list()
        for line in lines:
            line = line.strip()     # 消除每一行的\n
            line = line.split(",")  # 注意这里是英文逗号
            record = Record(line[0], line[1], line[2], line[3])
            records.append(record)
            print(record)   # 可选择不打印
        f.close()
        return records

class JSONFileReader(FileReader):

    def read_data(self) -> List[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        lines = f.readlines()
        records = list()
        for line in lines:
            record = json.loads(line)   # 此处JSON中的数据被解析为字典类型
            record = Record(record["date"], record["order_id"], record["money"], record["province"])
            records.append(record)
            print(record)   # 可选择不打印
        f.close()
        return records

def get_data(reader: FileReader) -> List[Record]:
    return reader.read_data()

if __name__ == "__main__":
    # file_path = "../../file/2011年1月销售数据.txt"
    # file_path = "../../file/2011年2月销售数据JSON.txt"
    # text_reader = TextFileReader(file_path)
    # json_reader = JSONFileReader(file_path)
    # text_reader.read_data()
    # json_reader.read_data()
    # 基于多态的方式实现数据读取
    file_path = "../../file/2011年1月销售数据.txt"
    text_reader = TextFileReader(file_path)
    data_list = get_data(text_reader)