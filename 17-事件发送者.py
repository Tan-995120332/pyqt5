#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
In this example, we determine the event sender
object.

author:Administrator
datetime:2018/3/17/017 23:34
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    # 在buttonClicked()方法中通过调用sender()方法来判断当前按下的是哪个按钮
    def initUI(self):
        # 创建了两个按钮
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)


        # 两个按钮连接到了同一个插槽
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    # 通过调用sender()方法来判断信号源， 并将其名称显示在窗体的状态栏中
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

