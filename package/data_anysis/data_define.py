"""
数据定义的类
"""
from typing import List


class Record:

    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        # print(f"日期为：{self.date}，ID为：{self.order_id}，金额为：{self.money}，省份为：{self.province}")
        return f"日期为：{self.date}，ID为：{self.order_id}，金额为：{self.money}，省份为：{self.province}"

class ProcessDate:

    def __init__(self, dataset):
        self.dataset: List[Record] = dataset

    def reshape_by_data(self) -> dict:
        data_by_day = dict()
        # 该思路不够优雅
        # for i in range(1, 3):
        #     date_month = "2011-0" + str(i)
        #     for j in range(1, 32):
        #         if j < 10:
        #             data_day = date_month + "-0" + str(j)
        #         else:
        #             data_day = date_month + "-" + str(j)
        #         data_by_day[data_day] = 0
        #         for data in self.dataset:
        #             if data_day == data.date:
        #                 data_by_day[data_day] += int(data.money)
        # 推荐使用该思路
        for data in self.dataset:
            if data.date in data_by_day.keys():
                data_by_day[data.date] += int(data.money)
            else:
                data_by_day[data.date] = int(data.money)
        return data_by_day