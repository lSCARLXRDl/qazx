import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.lw.itemClicked.connect(self.click)
        con = sqlite3.connect('coffe.sqlite')
        cur = con.cursor()
        res = cur.execute('''SELECT * FROM coffe''').fetchall()
        for i in res:
            item = QListWidgetItem(i[1])
            item.setTextAlignment(Qt.AlignHCenter)
            self.lw.addItem(item)
        con.commit()
        con.close()

    def click(self):
        global name
        name = self.lw.currentItem().text()
        con = sqlite3.connect('coffe.sqlite')
        cur = con.cursor()
        rez = f"SELECT * FROM coffe WHERE name = '{name}'"
        res = cur.execute(rez).fetchall()
        self.lbl1.setText(res[0][2])
        self.lbl2.setText(res[0][3])
        self.lbl3.setText(str(res[0][5]) + ' руб.')
        self.lbl4.setText(str(res[0][6]))
        self.te.setPlainText(res[0][4])
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())