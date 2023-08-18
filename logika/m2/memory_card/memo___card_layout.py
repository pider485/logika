''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
app = QApplication([])


btn_OK = QPushButton("Відповісти")
btn_sleep = QPushButton("Відпочити")
btn_menu= QPushButton("Меню")

lb_question = QLabel("")

box_minuts=QSpinBox()
box_minuts.setValue(5)

RadioGrupBox = QGroupBox('Варіанти відповідей')

RadioGrup= QButtonGroup()
r_btn1 = QRadioButton('')
r_btn2 = QRadioButton('')
r_btn3 = QRadioButton('')
r_btn4 = QRadioButton('')

RadioGrup.addButton(r_btn1)
RadioGrup.addButton(r_btn2)
RadioGrup.addButton(r_btn3)
RadioGrup.addButton(r_btn4)

Layout_ans1= QHBoxLayout()
Layout_ans2= QVBoxLayout()
Layout_ans3= QVBoxLayout()

Layout_ans2.addWidget(r_btn1)
Layout_ans2.addWidget(r_btn2)

Layout_ans3.addWidget(r_btn3)
Layout_ans3.addWidget(r_btn4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

RadioGrupBox.setLayout(Layout_ans1)

AnsGroupBox= QGroupBox()
lb_results= QLabel("")
lb_correct = QLabel("")

Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_results, alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(lb_correct, alignment=(Qt.AlignCenter), stretch=2)

AnsGroupBox.setLayout(Layout_res)

AnsGroupBox.hide()

Layout_card = QVBoxLayout()
Layout_line1= QHBoxLayout()
Layout_line2= QHBoxLayout()
Layout_line3= QHBoxLayout()
Layout_line4= QHBoxLayout()

Layout_line1.addWidget(btn_menu)
Layout_line1.addStretch(1)
Layout_line1.addWidget(btn_sleep)
Layout_line1.addWidget(box_minuts)
Layout_line1.addWidget(QLabel('хвилин'))

Layout_line2.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

Layout_line3.addWidget(RadioGrupBox)
Layout_line3.addWidget(AnsGroupBox)

Layout_line4.addStretch(1)
Layout_line4.addWidget(btn_OK)
Layout_line4.addStretch(1)

Layout_card.addLayout(Layout_line1)
Layout_card.addLayout(Layout_line2)
Layout_card.addLayout(Layout_line3)
Layout_card.addLayout(Layout_line4)





# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass