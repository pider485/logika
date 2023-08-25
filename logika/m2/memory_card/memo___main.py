from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будемо змішувати відповіді в картці питання
from memo___data import *

Radio_list = [r_btn1,r_btn2,r_btn3,r_btn4]

frm=Question('Apple','aples','aple','Яблуко','addd')

frm_card = QuestionView(frm, lb_question, Radio_list[0], Radio_list[1], Radio_list[2], Radio_list[3],)

card_width, card_height = 600, 500 # початкові розміри вікна "картка"

def show_data():
    ''' показує на екрані потрібну інформацію '''
    pass

def check_result():
    ''' перевірка, чи вибрана правильна відповідь 
    якщо відповідь була вибрана, то напис "правильно/не правильно" отримує потрібне значення
    і показує панель відповідів'''
    pass

win_card = QWidget()
win_card.resize(card_width, card_height)
#тут повинні бути параметри вікна
frm_card.show()
win_card.setLayout(Layout_card)
win_card.show()
app.exec_()