from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

app = QApplication([])
window =QWidget()

filed_text= QTextEdit()

lb_notes= QLabel('Список заміток')

lst_notes = QListWidget()

btn_note_create =QPushButton('Створити замітку')
btn_note_del =QPushButton('Видалити замітку')
btn_note_save =QPushButton('Зберегти замітку')



lb_teg= QLabel('Список тегів')

lst_teg = QListWidget()

filed_teg = QLineEdit()
btn_teg_add =QPushButton('Додати тег тег')
btn_teg_unPin =QPushButton('Відкріпити тег')
btn_teg_screach =QPushButton('Шукати тег')


layout_notes=QHBoxLayout()
col1= QVBoxLayout()
col2= QVBoxLayout()

layout_notes.addLayout(col1,stretch=2)
layout_notes.addLayout(col2,stretch=1)

row1= QHBoxLayout()
row2= QHBoxLayout()

col1.addWidget(filed_text)
col2.addWidget(lb_notes)

col2.addWidget(lst_notes)

row1.addWidget(btn_note_create)
row1.addWidget(btn_note_del)

col2.addLayout(row1)
col2.addWidget(btn_note_save)

col2.addWidget(lb_teg)

col2.addWidget(lst_teg)

col2.addLayout(row2)

row2.addWidget(btn_teg_add)
row2.addWidget(btn_teg_unPin)

col2.addWidget(btn_teg_screach)


def show_notes():
    key = lst_notes.selectedItems()[0].text()
    filed_text.setText(notes[key]['текст'])



lst_notes.itemClicked.connect(show_notes)



with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)
window.setLayout(layout_notes)
window.show()
app.exec_()
