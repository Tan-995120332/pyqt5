#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This example shows text which
is entered in a QLineEdit
in a QLabel widget.

author:Administrator
datetime:2018/3/18/018 14:30
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication

# 示例中展示了一个QLineEdit与一个QLabel。我们在QLineEdit中输入的文字会实时显示在QLabel控件中
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lb1 = QLabel(self)
        # 创建QLineEdit
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lb1.move(60, 40)
        # 文本框的内容发生改变的时候，会调用onChanged方法
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    # 在onChanged()方法中我们将QLabel控件的文本设置为输入的内容。
    def onChanged(self, text):

        self.lb1.setText(text)
        # 通过调用adjustSize()方法将QLabel控件的尺寸调整为文本的长度
        self.lb1.adjustSize()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

