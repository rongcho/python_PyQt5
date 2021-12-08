

import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QBasicTimer, Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.button = QPushButton('Start', self)
        self.button.move(40, 80)
        self.button.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0



        self.setWindowTitle("Progress Bar")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
