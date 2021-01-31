import sys
import sqlite3

from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget
from PyQt5.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(451, 481)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 421, 171))
        self.listWidget.setObjectName("listWidget")
        self.btn1 = QtWidgets.QPushButton(Form)
        self.btn1.setGeometry(QtCore.QRect(280, 420, 141, 28))
        self.btn1.setObjectName("btn1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 210, 61, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 210, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 255, 121, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 253, 41, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 31, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 298, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 350, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 400, 55, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 350, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 400, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(240, 210, 55, 16))
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(240, 230, 191, 131))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 180, 31, 28))
        self.pushButton.setObjectName("pushButton")

        Form.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn1.setText(_translate("Form", "Добавить/Изменить"))
        self.label.setText(_translate("Form", "Название:"))
        self.label_2.setText(_translate("Form", "Степень обжарки:"))
        self.comboBox.setItemText(0, _translate("Form", "I"))
        self.comboBox.setItemText(1, _translate("Form", "II"))
        self.comboBox.setItemText(2, _translate("Form", "III"))
        self.comboBox.setItemText(3, _translate("Form", "IV"))
        self.comboBox.setItemText(4, _translate("Form", "V"))
        self.label_3.setText(_translate("Form", "Тип:"))
        self.comboBox_2.setItemText(0, _translate("Form", "молотый"))
        self.comboBox_2.setItemText(1, _translate("Form", "в зёрнах"))
        self.label_4.setText(_translate("Form", "Цена:"))
        self.label_5.setText(_translate("Form", "Объём:"))
        self.label_6.setText(_translate("Form", "Вкус:"))
        self.pushButton.setText(_translate("Form", "+"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 489)
        self.cw = QtWidgets.QWidget(MainWindow)
        self.cw.setObjectName("cw")
        self.lw = QtWidgets.QListWidget(self.cw)
        self.lw.setGeometry(QtCore.QRect(40, 20, 371, 131))
        self.lw.setObjectName("lw")
        self.label = QtWidgets.QLabel(self.cw)
        self.label.setGeometry(QtCore.QRect(20, 200, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.cw)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.cw)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.cw)
        self.label_4.setGeometry(QtCore.QRect(20, 350, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.cw)
        self.label_5.setGeometry(QtCore.QRect(290, 200, 55, 16))
        self.label_5.setObjectName("label_5")
        self.te = QtWidgets.QPlainTextEdit(self.cw)
        self.te.setGeometry(QtCore.QRect(330, 200, 181, 91))
        self.te.setObjectName("te")
        self.lbl1 = QtWidgets.QLabel(self.cw)
        self.lbl1.setGeometry(QtCore.QRect(135, 200, 55, 16))
        self.lbl1.setText("")
        self.lbl1.setObjectName("lbl1")
        self.lbl2 = QtWidgets.QLabel(self.cw)
        self.lbl2.setGeometry(QtCore.QRect(55, 250, 55, 16))
        self.lbl2.setText("")
        self.lbl2.setObjectName("lbl2")
        self.lbl3 = QtWidgets.QLabel(self.cw)
        self.lbl3.setGeometry(QtCore.QRect(60, 300, 55, 16))
        self.lbl3.setText("")
        self.lbl3.setObjectName("lbl3")
        self.lbl4 = QtWidgets.QLabel(self.cw)
        self.lbl4.setGeometry(QtCore.QRect(70, 350, 55, 16))
        self.lbl4.setText("")
        self.lbl4.setObjectName("lbl4")
        self.btn2 = QtWidgets.QPushButton(self.cw)
        self.btn2.setGeometry(QtCore.QRect(450, 60, 171, 51))
        self.btn2.setObjectName("btn2")
        MainWindow.setCentralWidget(self.cw)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label_2.setText(_translate("MainWindow", "Цена:"))
        self.label_3.setText(_translate("MainWindow", "Тип:"))
        self.label_4.setText(_translate("MainWindow", "Объём:"))
        self.label_5.setText(_translate("MainWindow", "Вкус:"))
        self.btn2.setText(_translate("MainWindow", "Добавить/Изменить запись"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(QMainWindow, self)
        self.initUI()

    def initUI(self):
        self.lw.itemClicked.connect(self.click)
        self.btn2.clicked.connect(self.click1)
        con = sqlite3.connect('data/coffe.sqlite')
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
        con = sqlite3.connect('data/coffe.sqlite')
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


class Example1(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        Ui_Form.setupUi(QWidget, self)
        self.initUI()
        self.act = False

    def initUI(self):
        self.listWidget.itemClicked.connect(self.click)
        self.pushButton.clicked.connect(self.click1)
        self.btn1.clicked.connect(self.click2)
        con = sqlite3.connect('data/coffe.sqlite')
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
        con = sqlite3.connect('data/coffe.sqlite')
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
            con = sqlite3.connect('data/coffe.sqlite')
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

            con = sqlite3.connect('data/coffe.sqlite')
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
            con = sqlite3.connect('data/coffe.sqlite')
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

            con = sqlite3.connect('data/coffe.sqlite')
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