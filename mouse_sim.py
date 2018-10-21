import win32api
import win32con
import pyautogui
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QTextEdit
import sys
import time


# mouse_click(50, 50)
# mouse_click(50, 50)

print(pyautogui.position())


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.timeout = ''
        self.label = QLabel('', self)
        self.label.resize(self.label.width() * 2, self.label.height())
        self.text = QTextEdit(self)
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("CapturePosition", self)
        btn1.move(30, 50)

        btn1.clicked.connect(self.button1Clicked)

        self.statusBar()

        btn2 = QPushButton("StartTimer", self)
        btn2.move(30, 100)

        btn2.clicked.connect(self.button2Clicked)

        self.text.move(200, 100)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def button1Clicked(self):
        time.sleep(2)
        p = pyautogui.position()
        self.x = p[0]
        self.y = p[1]
        self.label.setText('Position:' + str(p))

    def button2Clicked(self):
        t = self.text.toPlainText()
        print('after:', t)
        time.sleep(int(t))
        pyautogui.click(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
