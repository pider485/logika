from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton)
app = QApplication([])
main_win=QWidget()
main_win.resize(200,200)
text = QLabel("2+2*2=?")
rbn_button1 =QRadioButton("4")
rbn_button2 =QRadioButton("6")
rbn_button3 =QRadioButton("8")
rbn_button4 =QRadioButton("10")


V_Line_1=QVBoxLayout()

H_Line_1=QHBoxLayout()
H_Line_2=QHBoxLayout()
H_Line_3=QHBoxLayout()

H_Line_1.addWidget(text,alignment=Qt.AlignCenter)
H_Line_2.addWidget(rbn_button1,alignment=Qt.AlignCenter)
H_Line_2.addWidget(rbn_button2,alignment=Qt.AlignCenter)
H_Line_3.addWidget(rbn_button3,alignment=Qt.AlignCenter)
H_Line_3.addWidget(rbn_button4,alignment=Qt.AlignCenter)

V_Line_1.addLayout(H_Line_1)
V_Line_1.addLayout(H_Line_2)
V_Line_1.addLayout(H_Line_3)

main_win.setLayout(V_Line_1)

def win():
    mesage_win=QMessageBox()
    mesage_win.setText("Молодець")
    mesage_win.exec_()
def lok():
    mesage_lok=QMessageBox()
    mesage_lok.setText("Не молодець")
    mesage_lok.exec_()
rbn_button1.clicked.connect(lok)
rbn_button2.clicked.connect(win)
rbn_button3.clicked.connect(lok)
rbn_button4.clicked.connect(lok)


main_win.show()
app.exec_()