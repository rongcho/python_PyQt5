import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp,QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime, Qt




class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.DateTime = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('클릭 시 창이 닫힙니다.')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar().showMessage(self.DateTime.toString(Qt.DefaultLocaleLongDate))
        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(exitAction)



        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&종료')
        filemenu.addAction(exitAction)



        self.setWindowTitle('종료버튼')
        self.setGeometry(300, 300, 300, 200)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())