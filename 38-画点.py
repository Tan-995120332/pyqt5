#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
In the example, we draw randomly 1000 red points
on the window.

author:Administrator
datetime:2018/3/18/018 16:49
software: PyCharm
'''

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

# 在这例子中，我们在窗口上随机绘制了1000个红点
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        # 设置画笔为红色，我们使用了预定义的Qt.red常量
        qp.setPen(Qt.red)
        # 每次我们改变窗口的大小, 生成一个paint event事件。
        # 我们得到的当前窗口的大小size。
        # 我们使用窗口的大小来分配点在窗口的客户区。
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            # 通过drawpoint绘制圆点
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())