#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
In this example, we dispay an image
on the window.

author:Administrator
datetime:2018/3/18/018 14:23
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap

# 在窗口上显示一个图片
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        # 创建一个QPixmap 对象，它将传入的文件名作为参数
        pixmap = QPixmap("logo.png")

        # 我们将这个pixmap放到QLabel控件中
        lb1 = QLabel(self)
        lb1.setPixmap(pixmap)

        hbox.addWidget(lb1)
        self.setLayout(hbox)

        self.move(300, 300)
        self.setWindowTitle('logo')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())