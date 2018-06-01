#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This example shows a QProgressBar widget.

author:Administrator
datetime:2018/3/18/018 14:05
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QWidget, QProgressBar,QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer

# 这个例子显示一个水平的进度条和一个按钮，用户通过点击按钮开始和停止进度条
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QProgressBar的构造方法
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # 我们使用定时器timer来激活QProgressBar
        self.time = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    # 每个QObject及其子类都有一个timerEvent()事件处理器。我们要重新实现这个事件处理器来响应定时器事件
    def timerEvent(self, e):

        if self.step >= 100:
            self.time.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    # 我们在doAction()方法中启动/停止定时器
    def doAction(self):

        if self.time.isActive():
            self.time.stop()
            self.btn.setText('Start')
        else:
            # 我们调用start()方法启动一个计时器。这个方法有两个参数: 超时和对象将接收的事件
            self.time.start(100, self)
            self.btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())