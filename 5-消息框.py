#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This program shows a confirmation
message box when we click on the close
button of the application window.
author:Administrator
datetime:2018/3/17/017 20:00
software: PyCharm
'''

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 255, 150)
        self.setWindowTitle('Message box')
        self.show()

    # 关闭窗口的时候, 触发了QCloseEvent,需要重写closeEvent()事件处理程序
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())