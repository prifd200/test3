from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from shifr import *
def lk():
    Form3, Window3 = uic.loadUiType("личный кабинет.ui")
    window3 = Window3()
    form3 = Form3()
    form3.setupUi(window3)
    window3.show()
    if form3.pushButton.clicked:
        file2 = open("зашифровка.txt", "w")
        #file2.write(encrypt(form3.lineEdit_2.toPlainText().lower()))
        file2.close()
    if form3.pushButton_2.clicked:
        file3 = open(" расшифровка.txt", "w")
        #file3.write(encrypt(form3.lineEdit_2.toPlainText().lower()))
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
            return "exit"

def login():
    Form, Window = uic.loadUiType("main.ui")
    window1 = Window()
    form1 = Form()
    form1.setupUi(window1)
    window1.show()
    app.exec()
    form1.pushButton.clicked.connect(lk)
    if form1.pushButton.clicked:
        with open("data.txt", "r+") as d:
            if f"логин: {form1.lineEdit.text()}\nпароль: {form1.lineEdit_2.text()}" in d.read():
                window1.close()
                lk()
            else:
                form1.plainTextEdit.setPlainText("Неверный логин или пароль")
    if form1.pushButton_2.clicked:
        Form2, Window2 = uic.loadUiType("регистрация.ui")
        window2 = Window2()
        form2 = Form2()
        form2.setupUi(window2)
        window2.show()
        window1.close()
        form = open("data.txt", "w+")
        #form.write(encrypt(form2.lineEdit.displayText()))  # Запись в файл зашифрованного логина
        #form.write('\n')
        #form.write(encrypt(form2.lineEdit_2.displayText()))  # Запись в файл зашифрованного пароля
        form.close()
        #if form2.pushButton.clicked:
            #login()
app = QApplication([])

login()
#def start():
    #if login() == "exit":
sys.exit(app.exec())
        #return None
    #else:
        #start()

#start()