#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
In this example, we reimplement an
event handler.

author:Administrator
datetime:2018/3/17/017 23:29
software: PyCharm
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        # 重新实现了keyPressEvent()事件处理器,按下Escape键会使程序退出
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
