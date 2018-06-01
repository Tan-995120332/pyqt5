#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
In this example, we create a skeleton
of a calculator using a QGridLayout.

author:Administrator
datetime:2018/3/17/017 21:28
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 表格布局将空间划分为行和列。我们使用QGridLayout类创建一个网格布局
        grid = QGridLayout()
        self.setLayout(grid)
        # 按钮的标签
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        # 创建一个网格中的位置的列表
        positions = [(i,j) for i in range(5) for j in range(4)]

        # 创建按钮并使用addWidget()方法添加到布局中
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)


        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())