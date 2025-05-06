"""
和文件相关的类定义
"""
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts, LabelOpts


class VisualData:

    def __init__(self, data: dict):
        self.data: dict = data

    def bar(self):
        keys = list(self.data.keys())
        values = list(self.data.values())
        # 创建柱状图对象
        # 写法一
        # bar = (
        #     Bar()
        #     .add_xaxis(keys)
        #     .add_yaxis("销售额", values)
        #     .set_global_opts(
        #         title_opts=opts.TitleOpts(title="日销售额可视化表"),
        #         toolbox_opts=opts.ToolboxOpts(is_show=True)
        #     )
        # )
        # 写法二
        bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis( keys)
        bar.add_yaxis("销售额", values, label_opts=LabelOpts(is_show=False))
        bar.set_global_opts(
            title_opts=opts.TitleOpts(title="日销售额可视化表"),
            toolbox_opts=opts.ToolboxOpts(is_show=True)
        )

        # 渲染图表到 HTML 文件
        bar.render("../charts/bar_chart.html")