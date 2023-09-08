from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle  # перемішуватимемо відповіді у картці питання

from memo___card_layout import *
from memo___main_layout import *
from memo___edit_layout import *
from memo___data import *

main_width, main_height = 1000, 450  # початкові розміри головного вікна
card_width, card_height = 600, 500  # початкові розміри вікна "картка"
time_unit = 60000


radio_list = [r_btn1, r_btn2, r_btn3, r_btn4]

questions_listmodel = QuestionListModel()  # список запитань
# запам'ятовуємо, що у формі редагування питання з чим пов'язано
frm_edit = QuestionEdit(0, txt_Question, txt_Answer,
                        txt_Wrong1, txt_Wrong2, txt_Wrong3)
frm_card = 0  # тут буде зв'язуватися питання з формою тесту
timer = QTimer()
win_main = QWidget()
win_card = QWidget()


# Тестові данні
def testlist():

    frm = Question('2+2*2', '6', '4', '8', '10')
    questions_listmodel.form_list.append(frm)
    frm = Question('1+1', '2', '3', '4', 'да')
    questions_listmodel.form_list.append(frm)
    frm = Question('Якщо безпосередньо вивчити об’єкт (явище) з деяких причин не можливо, застосовують метод -', 'моделювання', 'порівнювання', 'спостереження', 'демонстрації')
    questions_listmodel.form_list.append(frm)
    frm = Question('Винахід - це', 'щось нове(корисний у господарській діяльності пристрій, який можна використати на практиці.', 'забута річ', 'щось нове(корисний у господарській діяльності пристрій, який НЕ можна використати на практиці.', '')
    questions_listmodel.form_list.append(frm)
    frm = Question('На полу ліфта стоїть валіза масою 12 кг. Виберіть правильне твердження.', 'Якщо ліфт рушає з нижнього поверху, сила реакції підлоги більша ніж 120 Н.', 'Якщо ліфт нерухомий, сила реакції підлоги більша ніж 120 Н.', 'Чим більше прискорення руху ліфта, тим більша сила тяжіння діє на валізу.', 'Якщо ліфт рушає з верхнього поверху, сила реакції підлоги більша ніж 120 Н.')
    questions_listmodel.form_list.append(frm)
    frm = Question('Чи правда, що дріб 1/3 = 1, (3) ?', 'ні', 'так', 'частково', 'незнаю')
    questions_listmodel.form_list.append(frm)
    frm = Question('Який із кутів є прямим?', 'кут 90 градусів', 'кут 30 градусів', 'кут 173 градуси', 'кут 180 градусів')
    questions_listmodel.form_list.append(frm)
    frm = Question('Столицею якої країни є Джакарта?', 'Індонезія', 'Східний Тімор', 'Сінгапур', 'Малайзія')
    questions_listmodel.form_list.append(frm)
    frm = Question('Столицею якої країни є Ліма?', 'Перу', 'Гаяна', 'Колумбія', 'Еквадор')
    questions_listmodel.form_list.append(frm)
    frm = Question('Які складові частини повного імені файла?', 'шлях до файла + ім`я файла', 'шлях до файла + тип файла', 'список + ім`я файла', 'адреса + розширення')
    questions_listmodel.form_list.append(frm)


# Функції для проведення тесту


def set_card():
    ''' задає, який вигляд має вікно картки'''
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(Layout_card)


def set_main():
    ''' задає, який вигляд має основне вікно'''
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle('Список питань')
    win_main.setLayout(layout_main)


def sleep_card():
    ''' картка ховається на час, зазначений у таймері'''
    win_card.hide()
    timer.setInterval(time_unit * box_minuts.value())
    timer.start()


def show_card():
    ''' показує вікно (за таймером), таймер зупиняється'''
    win_card.show()
    timer.stop()


def show_random():
    ''' показати випадкове запитання '''
    global frm_card
    frm_card = random_AnswerCheck(questions_listmodel, lb_question, radio_list, lb_correct, lb_results)
    frm_card.show()
    show_question()


def click_OK():
    ''' перевіряє запитання або завантажує нове запитання '''
    if btn_OK.text() != 'Наступне питання':
        frm_card.check()
        show_result()
    else:
        # напис на кнопці дорівнює 'Наступний', ось і створюємо наступне випадкове запитання:
        show_random()


def back_to_menu():
    ''' повернення з тесту у вікно редактора '''
    win_card.hide()
    win_main.showNormal()

# Функції для редагування питань


def edit_question(index):
    ''' завантажує у форму редагування запитання і відповіді, що відповідають переданому рядку '''

    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()


def add_form():
    ''' додає нове запитання і пропонує його змінити '''
    questions_listmodel.insertRows()
    last = questions_listmodel.rowCount(0) - 1

    index = questions_listmodel.index(last)
    list_questions.setCurrentIndex(index)
    edit_question(index)
    txt_Question.setFocus(Qt.TabFocusReason)


def del_form():
    ''' видаляє питання і перемикає фокус '''
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())


def start_test():
    ''' на початку тесту форма зв'язується з випадковим питанням і показується '''
    show_random()
    win_card.show()
    win_main.showMinimized()

# Встановлення потрібних з`єднань


def connects():
    list_questions.setModel(questions_listmodel)
    list_questions.clicked.connect(edit_question)
    btn_add.clicked.connect(add_form)
    btn_delete.clicked.connect(del_form)
    btn_start.clicked.connect(start_test)
    btn_OK.clicked.connect(click_OK)
    btn_menu.clicked.connect(back_to_menu)
    timer.timeout.connect(show_card)
    btn_sleep.clicked.connect(sleep_card)


testlist()
set_card()
set_main()
connects()
win_main.show()
app.exec_()
