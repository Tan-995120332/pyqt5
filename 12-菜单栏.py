#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This program creates a menubar. The
menubar has one menu with an exit action.

author:Administrator
datetime:2018/3/17/017 22:11
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个菜单栏和一个菜单。这个菜单将终止应用程序

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')  # 设置快捷方式
        exitAction.setStatusTip('Exit application') # 创建一个鼠标指针悬停在该菜单项上时的提示
        exitAction.triggered.connect(qApp.quit)  # 调用qApp.quit,终止应用程序

        self.statusBar()

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 添加事件
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




