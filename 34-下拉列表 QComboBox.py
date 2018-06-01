#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This example shows how to use
a QComboBox widget.


author:Administrator
datetime:2018/3/18/018 14:44
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)

'''
示例中展示了一个QComboBox与一个QLabel，
QComboBox控件中有5个选项(Linux系统的几个发行版名称)。
QLabel控件会显示QComboBox中选中的某个选项
'''
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel("Ubuntu", self)
        # 创建了一个有五个选项的QComboBox
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)
        # 当选中某个条目时会调用onActivated()方法。
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    # 在方法中我们将QLabel控件的内容设置为选中的条目，然后调整它的尺寸
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())