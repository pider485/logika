from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json


def writeToFile():
    with open('notes.json', 'w', encoding='utf8')as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)

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

col2.addWidget(filed_teg)

col2.addLayout(row2)

row2.addWidget(btn_teg_add)
row2.addWidget(btn_teg_unPin)

col2.addWidget(btn_teg_screach)


def show_notes():
    key = lst_notes.selectedItems()[0].text()
    filed_text.setText(notes[key]['текст'])

    lst_teg.clear()
    lst_teg.addItems(notes[key]['теги'])


def add_note():
    note_name , ok = QInputDialog.getText(window,'Додати замітку', 'Назва замітки')
    if note_name and ok:
        lst_notes.addItem(note_name)
        notes[note_name] = {"текст": "","теги": []}



    writeToFile()

def del_note():
    if lst_notes.currentItem():    
        key = lst_notes.currentItem().text()
        del notes[key]
        writeToFile()
        filed_teg.clear()
        lst_teg.clear()
        lst_notes.clear()
        lst_notes.addItems(notes)

def save_notes():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()

        notes[key]['текст']  = filed_text.toPlainText()
        writeToFile()


def add_teg():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        teg = filed_teg.text()
        notes[key]['теги'].append(teg)

        lst_teg.addItem(teg)
        writeToFile()

def del_teg():
    key = lst_notes.currentItem().text()
    teg = lst_teg.currentItem().text()
        
    notes[key]['теги'].remove(teg)
    
    lst_teg.clear()
    lst_teg.addItems(notes[key]['теги'])
    
    writeToFile()

def search_teg():
    teg = filed_teg.text()

    if 'Шукати тег' == btn_teg_screach.text():
        filtered_notes= {}

        for key in notes:
            if teg in notes[key]['теги']:
                filtered_notes[key] = notes[key]
        
        btn_teg_screach.setText('Скинути пошук')

        lst_notes.clear()
        lst_notes.addItems(filtered_notes)
        lst_teg.clear()
        filed_text.clear()

    elif 'Скинути пошук' == btn_teg_screach.text():
        btn_teg_screach.setText('Шукати тег')

        lst_notes.clear()
        lst_notes.addItems(notes)
        lst_teg.clear()
        filed_text.clear()
        filed_teg.clear()


btn_note_save.clicked.connect(save_notes)

btn_note_del.clicked.connect(del_note)

btn_note_create.clicked.connect(add_note)

lst_notes.itemClicked.connect(show_notes)


btn_teg_add.clicked.connect(add_teg)
btn_teg_unPin.clicked.connect(del_teg)
btn_teg_screach.clicked.connect(search_teg)

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)
window.setLayout(layout_notes)
window.show()
app.exec_()
