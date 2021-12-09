

import sys
from PyQt5.QtWidgets import QApplication,QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime, Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)


        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(),0,1)
        grid.addWidget(QLineEdit(),1,1)
        grid.addWidget(QTextEdit(),2,1)


        self.setWindowTitle('Grid Layout')
        self.setGeometry(500, 500, 400, 300)
        self.show()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())

