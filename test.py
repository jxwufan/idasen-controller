from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import argparse
import desk
import logging
import asyncio
app = QApplication([])
window = QWidget()
glayout = QGridLayout()
label1 = QLabel("1")
edit1 = QLineEdit("0")
button1 = QPushButton("Move")
label2 = QLabel("2")
edit2 = QLineEdit("0")
button2 = QPushButton("Move")
label3 = QLabel("3")
edit3 = QLineEdit("0")
button3 = QPushButton("Move")
label4 = QLabel("4")
edit4 = QLineEdit("0")
button4 = QPushButton("Move")
glayout.addWidget(label1, 0, 0, alignment=QtCore.Qt.AlignHCenter)
glayout.addWidget(edit1, 1, 0)
glayout.addWidget(button1, 2, 0)
glayout.addWidget(label2, 0, 1, alignment=QtCore.Qt.AlignHCenter)
glayout.addWidget(edit2, 1, 1)
glayout.addWidget(button2, 2, 1)
glayout.addWidget(label3, 0, 2, alignment=QtCore.Qt.AlignHCenter)
glayout.addWidget(edit3, 1, 2)
glayout.addWidget(button3, 2, 2)
glayout.addWidget(label4, 0, 3, alignment=QtCore.Qt.AlignHCenter)
glayout.addWidget(edit4, 1, 3)
glayout.addWidget(button4, 2, 3)
window.setLayout(glayout)

bt_desk = desk.IdasenDesk("C7:A8:48:D5:E9:0E")
loop = asyncio.get_event_loop()
loop.run_until_complete(bt_desk._connect_and_validate())
loop.run_until_complete(bt_desk.move_to(0))

def on_button_clicked1():
    loop.run_until_complete(bt_desk.move_to(int(edit1.text())))
def on_button_clicked2():
    loop.run_until_complete(bt_desk.move_to(int(edit2.text())))
def on_button_clicked3():
    loop.run_until_complete(bt_desk.move_to(int(edit3.text())))
def on_button_clicked4():
    loop.run_until_complete(bt_desk.move_to(int(edit4.text())))

button1.clicked.connect(on_button_clicked1)
button2.clicked.connect(on_button_clicked2)
button3.clicked.connect(on_button_clicked3)
button4.clicked.connect(on_button_clicked4)
window.show()
app.exec_()