from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from shifr import *

Form, Window = uic.loadUiType("main.ui")
app = QApplication([])
window1 = Window()
form1 = Form()
form1.setupUi(window1)
window1.show()
def login():
    def lk():
        global window3
        Form3, Window3 = uic.loadUiType("личный кабинет.ui")
        window3 = Window3()
        form3 = Form3()
        form3.setupUi(window3)
        window3.show()
        if form3.pushButton.clicked:
            file2 = open("зашифровка.txt", "w")
            file2.close()
        if form3.pushButton_2.clicked:
            file3 = open(" расшифровка.txt", "w")
            file3.close()
        if form3.pushButton_3.clicked:
            Form4, Window4 = uic.loadUiType("выход.ui")
            window4 = Window4()
            form4 = Form4()
            form4.setupUi(window4)
            window4.show()
            if form4.pushButton_2.clicked:
                window4.close()
            if form4.pushButton.clicked:
                window4.close()
                window3.close()
                window1.show()
        form3.pushButton_3.clicked.connect(lk)
        form3.pushButton_2.clicked.connect(lk)
        form3.pushButton.clicked.connect(lk)
    def auth():
        d = open("data.txt", "r+")
        if f"логин: {form1.lineEdit.text()}\nпароль: {form1.lineEdit_2.text()}" in d.read():
            lk()
            d.close()
        else:
            form1.plainTextEdit.setPlainText("Неверный логин или пароль")

    def reg():
        Form2, Window2 = uic.loadUiType("регистрация.ui")
        window2 = Window2()
        form2 = Form2()
        form2.setupUi(window2)
        window2.show()
        window1.close()
        form = open("data.txt", "a+")
        def du():
            if form2.lineEdit_2.displayText() != " " and form2.lineEdit_3.displayText() != " ":
                with open("data.txt", "r+") as d:
                    if f"логин: {form2.lineEdit_2.displayText()}\n" in d.read():
                        form2.lineEdit.setText("Пользователь уже существует")
                    else:
                        form.write(f"\nлогин: {form2.lineEdit_2.displayText()}\nпароль: {form1.lineEdit_2.text()}")
                        window2.close()
                        lk()

        form2.pushButton_2.clicked.connect(du)
        form2.pushButton.clicked.connect(login)
        form.close()
    form1.pushButton_2.clicked.connect(reg)
    form1.pushButton.clicked.connect(auth)


form1.pushButton.clicked.connect(login)

app.exec_()
