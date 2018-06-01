#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/3/17/017 18:46
# software: PyCharm
# This example shows an icon
# in the titlebar of the window

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# 继承自QWidget类
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUi方法
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Inoc')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('logo.png'))

        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())





