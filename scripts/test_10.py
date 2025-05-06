"""
本代码用于Python的零基础学习
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 面向对象的编程案例 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ###
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 数据分析案例 ##########################################################################################################
# 设计需求：
#   某公司有两份数据文件，现需要对其进行分析处理，计算每日的销售额并以柱状图表的形式进行展示
#   一月份数据是普通文本，使用逗号分隔数据记录，从前到后分别是日期，订单id，销售额，销售省份
#   二月份数据是JSON数据，同样包含日期，订单id，销售额，销售省份
# 设计思路：
#   读取文件类：读取txt或者JSON格式的文件，然后将每一行保存为一个类对象，整个文件的数据保存为一个元素类型为类对象的列表
#   数据处理类：将数据进行处理，最终得到一个字典，key为某天，value为当天销售额
#   图表绘制类：使用pyecharts将销售额可视化为柱状图
#-----------------------------------------------------------------------------------------------------------------------

from package.data_anysis.data_define import *
from package.data_anysis.file_define import *
from package.data_anysis.chart_define import *


if __name__ == "__main__":
    # 基于多态的方式实现数据读取
    text_reader = TextFileReader("../file/2011年1月销售数据.txt")
    json_reader = JSONFileReader("../file/2011年2月销售数据JSON.txt")
    jan_data: List[Record] = get_data(text_reader)
    feb_data: List[Record] = get_data(json_reader)
    all_data = jan_data + feb_data

    # 将销售额按日进行汇总
    pro_data = ProcessDate(all_data)
    data_reshape = pro_data.reshape_by_data()
    print(data_reshape)

    # 可视化数据
    visual_data = VisualData(data_reshape)
    visual_data.bar()

