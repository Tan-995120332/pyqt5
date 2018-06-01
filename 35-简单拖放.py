#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This is a simple drag and
drop example.

author:Administrator
datetime:2018/3/18/018 16:01
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QPushButton, QWidget,QLineEdit, QApplication

# 需要重新实现某些方法才能使QPushButton接受拖放操作。因此我们创建了继承自QPushButton的Button类
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        # 使该控件接受drop(放下)事件
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        # 首先我们重新实现了dragEnterEvent()方法，并设置可接受的数据类型(在这里是普通文本)
        if e.mimeData().hasFormat('f:/'):
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        # 通过重新实现dropEvent()方法，我们定义了在drop事件发生时的行为。这里我们改变了按钮的文字。
        self.setText(e.mimeData().text())

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QLineEdit内置了对drag(拖动)操作的支持。我们只需要调用setDragEnabled()方法就可以了
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(220, 65)

        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

