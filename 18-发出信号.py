
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
In this example, we determine the event sender
object.

author:Administrator
datetime:2018/3/17/017 23:49
software: PyCharm
'''

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

# 信号closeApp是Communicate的类属性，它由pyqtSignal()创建
class Communicate(QObject):

    closeApp = pyqtSignal()

# 创建了一个名为closeApp的信号。这个信号会在按下鼠标时触发，它连接着QMainWindow的close()插槽
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 自定义closeApp信号连接到QMainWindow的close槽
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        # 当在窗体上点击鼠标时会触发closeApp信号，使程序退出
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())