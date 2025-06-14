import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import cv2
import os

print("########################################################")
print(os.getcwd())
print("########################################################")

class PracticeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # pushbutton 생성
        self.btn1 = QPushButton("New_Window")
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.clicked.connect(self.new_window)

        self.btn2 = QPushButton("This_Window")
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.clicked.connect(self.this_window)
        self.btn2_temp = 0

        self.btn3 = QPushButton("New_Window_Video")
        self.btn3.clicked.connect(self.new_window_video)

        # image 불러오기
        self.image = cv2.imread("study\\data\\bom.jpg", cv2.IMREAD_COLOR)
        self.pixmap = QPixmap("study\\data\\bom.jpg")
        self.pixmap = self.pixmap.scaled(530, 707, Qt.KeepAspectRatio)
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)
        self.label.hide()

        # layout
        self.grid = QGridLayout()
        self.grid.addWidget(QLabel("이미지를 새 창에 띄우기: "), 0, 0)
        self.grid.addWidget(self.btn1, 0, 1)
        self.grid.addWidget(QLabel("이미지를 현재 창에 띄우기: "), 1, 0)
        self.grid.addWidget(self.btn2, 1, 1)
        self.grid.addWidget(self.label, 2, 1)
        self.grid.addWidget(QLabel("비디오를 새 창에 띄우기: "), 3, 0)
        self.grid.addWidget(self.btn3, 3, 1)

        # widget 배치
        self.widget = QWidget()
        self.widget.setLayout(self.grid)
        self.setCentralWidget(self.widget)

        self.setWindowTitle("MyWindow")
        self.move(300, 300)
        self.show()

    # 새 창에 이미지 띄우기
    def new_window(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # 현재 창에 이미지 띄우기
    def this_window(self):
        self.btn2_temp = not self.btn2_temp
        if self.btn2_temp:
            self.label.show()
        else:
            self.label.hide()

    # 새 창에 비디오 띄우기
    def new_window_video(self):
        video = cv2.VideoCapture("study\\data\\video.mp4")

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            cv2.imshow("New Window for Video", frame)
            if cv2.keyWait(25) == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PracticeApp()
    sys.exit(app.exec_())
