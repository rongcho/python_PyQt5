

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime, Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

#버튼에 단축키 : 앰퍼샌드 (ampersand, &) / Art + 첫글자 단어
#setCheckable()을 True - 선택되거나 선택되지 않은 상태 유지
#toggle() 메서드를 호출하면 버튼의 상태가 변경됨. 따라서 이 버튼은 프로그램이 시작될 때 선택되어 있음


#상태유지 버튼
    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()
#일반 버튼
        btn2 = QPushButton(self)
        btn2.setText('Button&2')
#버튼 비활성화
        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)


        self.setLayout(vbox)
        self.setWindowTitle('오올')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())