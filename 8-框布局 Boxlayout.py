#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
In this example, we position two push
buttons in the bottom-right corner
of the window.
author:Administrator
datetime:2018/3/17/017 20:55
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancle')
        # 创建一个水平布局和添加一个伸展因子和两个按钮
        hbox = QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

