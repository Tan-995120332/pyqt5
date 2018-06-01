#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
In this example, we determine the event sender
object.

author:Administrator
datetime:2018/3/18/018 13:03
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

# 在我们的示例中,我们将创建一个复选框,将切换窗口标题
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 这是QCheckBox的构造函数
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        # 我们有设置窗口标题,所以我们也必须检查复选框。默认情况下,没有设置窗口标题和也没有勾选复选框
        cb.toggle()
        # 我们将自定义的changeTitle()方法连接到stateChanged信号。这个方法会切换窗体的标题
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):
        # 复选框的状态经由state参数传入changeTitle()方法。
        # 在勾选复选框时设置窗体标题，取消勾选时就将标题设为空字符串
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())