from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
import random
from PyQt5 import uic


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.draw = False
        self.circles = []
        self.pushButton.clicked.connect(self.circle)

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.paint(qp)
            qp.end()
            self.draw = False

    def paint(self, qp):
        yellow = QColor.fromRgb(255, 255, 0)
        qp.setBrush(QBrush(yellow))
        qp.setPen(QPen(yellow))
        for x, y, r in self.circles:
            qp.drawEllipse(x, y, r, r)

    def circle(self):
        self.draw = True
        self.circles.append((random.randint(0, self.geometry().width()),
                             random.randint(0, self.geometry().height()),
                            random.randint(0, 100)))
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
