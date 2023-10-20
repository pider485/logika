import os

# потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap  # оптимізована для показу на екрані картинка
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel, 
    QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
)



app = QApplication([])
main_win = QWidget()

btn_folder = QPushButton('Папка')
btn_left = QPushButton('Ліво')
btn_right = QPushButton('Право')
btn_flip = QPushButton('Дзеркало')
btn_sharp = QPushButton('Різкість')
btn_bw = QPushButton('ЧБ')

lst_files = QListWidget()
lb_pic= QLabel('Картинки')

layout_editor=QHBoxLayout()
row= QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(lst_files)

col2.addWidget(lb_pic)
row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_flip)
row.addWidget(btn_sharp)
row.addWidget(btn_bw)


col2.addLayout(row)

layout_editor.addLayout(col1, 1)
layout_editor.addLayout(col2, 4)

wordir = QFileDialog.getExistingDirectory()


files_and_folders = os.listdir(wordir)

print(files_and_folders)

def filter(files):
    result = []
    ext = ['jpg', 'jpeg', 'bmp', 'gif', 'jfif', 'svg', 'png']
    
    for file in files:
        if file.split('.')[-1] in ext:
            result.append(file)
    return result

result=filter(files_and_folders)
print(result)


main_win.setLayout(layout_editor)
main_win.show()
app.exec()
