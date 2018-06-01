#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This example shows a QSlider widget.

author:Administrator
datetime:2018/3/18/018 13:26
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

# 例子中我们模拟了一个音量控制。通过拖动滑块来改变标签上的图像
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个水平滑块
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        # 我们将valueChanged信号连接到自定义的changeValue()方法
        sld.valueChanged[int].connect(self.changeValue)

        # 创建了一个QLabel控件并为它设置了一个初始音量图像
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('audio.ico'))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        # 根据滑动条的值来设置标签的图像。在上面的代码中，当滑动条的值为0时我们为标签设置audio.ico图像
        if value == 0:
            self.label.setPixmap(QPixmap('audio.ico'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.ico'))
        elif value > 30 and value <= 80:
            self.label.setPixmap(QPixmap('med.ico'))
        else:
            self.label.setPixmap(QPixmap('max.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
