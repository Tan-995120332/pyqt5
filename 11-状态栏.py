#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This program creates a statusbar.

author:Administrator
datetime:2018/3/17/017 22:04
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 用QMainWindow创建状态栏的小窗口
        # 后续调用返回的状态栏对象。showMessage()状态栏上显示一条消息
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())