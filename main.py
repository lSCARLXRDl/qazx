import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.lw.itemClicked.connect(self.click)
        self.btn2.clicked.connect(self.click1)
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

    def click1(self):
        self.w = Example1()
        self.w.show()


class Example1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUI()
        self.act = False

    def initUI(self):
        self.listWidget.itemClicked.connect(self.click)
        self.pushButton.clicked.connect(self.click1)
        self.btn1.clicked.connect(self.click2)
        con = sqlite3.connect('coffe.sqlite')
        cur = con.cursor()
        res = cur.execute('''SELECT * FROM coffe''').fetchall()
        for i in res:
            item = QListWidgetItem(i[1])
            item.setTextAlignment(Qt.AlignHCenter)
            self.listWidget.addItem(item)
        con.commit()
        con.close()

    def click(self):
        self.act = True
        global name
        name = self.listWidget.currentItem().text()
        con = sqlite3.connect('coffe.sqlite')
        cur = con.cursor()
        rez = f"SELECT * FROM coffe WHERE name = '{name}'"
        res = cur.execute(rez).fetchall()
        self.lineEdit.setText(name)
        self.comboBox.setCurrentText(res[0][2])
        self.comboBox_2.setCurrentText(res[0][3])
        self.lineEdit_2.setText(str(res[0][5]))
        self.lineEdit_3.setText(str(res[0][6]))
        self.plainTextEdit.setPlainText(res[0][4])
        con.commit()
        con.close()

    def click1(self):
        self.act = False
        self.lineEdit.setText('')
        self.comboBox.setCurrentText('I')
        self.comboBox_2.setCurrentText('молотый')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.plainTextEdit.setPlainText('')

    def click2(self):
        if self.act:
            con = sqlite3.connect('coffe.sqlite')
            cur = con.cursor()
            a = f"UPDATE coffe SET name = '{self.lineEdit.text()}' WHERE name = '{name}'"
            cur.execute(a)
            a = f"UPDATE coffe SET obj = '{self.comboBox.currentText()} 'WHERE name = '{name}'"
            cur.execute(a)
            a = f"UPDATE coffe SET type = '{self.comboBox_2.currentText()}' WHERE name = '{name}'"
            cur.execute(a)
            a = f"UPDATE coffe SET flavor = '{self.plainTextEdit.toPlainText()}' WHERE name = '{name}'"
            cur.execute(a)
            a = f"UPDATE coffe SET price = {int(self.lineEdit_2.text())} WHERE name = '{name}'"
            cur.execute(a)
            a = f"UPDATE coffe SET volume = {float(self.lineEdit_3.text())} WHERE name = '{name}'"
            cur.execute(a)
            self.listWidget.clear()
            res = cur.execute('''SELECT * FROM coffe''').fetchall()
            for i in res:
                item = QListWidgetItem(i[1])
                item.setTextAlignment(Qt.AlignHCenter)
                self.listWidget.addItem(item)
            con.commit()
            con.close()

            con = sqlite3.connect('coffe.sqlite')
            cur = con.cursor()
            res = cur.execute('''SELECT * FROM coffe''').fetchall()
            ex.lw.clear()
            for i in res:
                item = QListWidgetItem(i[1])
                item.setTextAlignment(Qt.AlignHCenter)
                ex.lw.addItem(item)
            con.commit()
            con.close()
        else:
            con = sqlite3.connect('coffe.sqlite')
            cur = con.cursor()
            a = f"INSERT INTO coffe(name, obj, type, flavor, price, volume) VALUES('{self.lineEdit.text()}'," \
                f" '{self.comboBox.currentText()}', '{self.comboBox_2.currentText()}'," \
                f" '{self.plainTextEdit.toPlainText()}', {int(self.lineEdit_2.text())}," \
                f" {float(self.lineEdit_3.text())})"
            cur.execute(a)
            self.listWidget.clear()
            res = cur.execute('''SELECT * FROM coffe''').fetchall()
            for i in res:
                item = QListWidgetItem(i[1])
                item.setTextAlignment(Qt.AlignHCenter)
                self.listWidget.addItem(item)
            con.commit()
            con.close()

            con = sqlite3.connect('coffe.sqlite')
            cur = con.cursor()
            res = cur.execute('''SELECT * FROM coffe''').fetchall()
            ex.lw.clear()
            for i in res:
                item = QListWidgetItem(i[1])
                item.setTextAlignment(Qt.AlignHCenter)
                ex.lw.addItem(item)
            con.commit()
            con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())