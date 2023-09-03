from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle

# такий рядок встановлюватиметься за замовчуванням для нових запитань
new_quest_templ = 'Нове запитання'
new_answer_templ = 'Нова відповідь'  # те саме для відповідей

text_wrong = 'Не правильно'
text_correct = 'Правильно'


class Question():
    ''' зберігає інформацію про одне питання'''

    def __init__(self, question=new_quest_templ, answer=new_answer_templ,
                 wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        self.question = question  # питання
        self.answer = answer  # правильна відповідь
        # вважаємо, що завжди пишеться три невірні варіанти
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True  # чи продовжувати ставити це запитання?
        self.attempts = 0  # скільки разів це запитання ставилося
        self.correct = 0  # кількість правильних відповідей

    def got_right(self):
        ''' змінює статистику, отримавши правильну відповідь'''
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        ''' змінює статистику, отримавши неправильну відповідь'''
        self.attempts += 1


class QuestionView():
    ''' зіставляє дані та віджети для відображення запитання'''

    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # конструктор отримує і запам'ятовує об'єкт із даними та віджети, що відповідають полям анкети
        self.frm_model = frm_model  # може отримати і None - нічого страшного не трапиться,
        # але для методу show потрібно буде попередньо оновити дані методом change
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def change(self, frm_model):
        ''' оновлення даних, уже пов'язаних з інтерфейсом '''
        self.frm_model = frm_model

    def show(self):
        ''' виводить на екран усі дані з об'єкта '''
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)


class QuestionEdit(QuestionView):
    ''' використовується, якщо потрібно редагувати форму: встановлює обробники подій, які зберігають текст'''

    def save_question(self):
        ''' зберігає текст запитання '''
        self.frm_model.question = self.question.text() 

    def save_answer(self):
        ''' зберігає текст правильної відповіді '''
        self.frm_model.answer = self.answer.text()  

    def save_wrong(self):
        ''' зберігає всі неправильні відповіді
        (якщо в наступній версії програми кількість неправильних відповідей стане змінною
        і вони будуть вводитися в списку, можна буде поміняти цей метод) '''
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()

    def set_connects(self):
        ''' встановлює обробки подій у віджетах так, щоб зберігати дані '''
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_answer1.editingFinished.connect(self.save_wrong)
        self.wrong_answer2.editingFinished.connect(self.save_wrong)
        self.wrong_answer3.editingFinished.connect(self.save_wrong)

    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.set_connects()






class AnswerCheck(QuestionView):
    ''' вважаючи, що питання анкети візуалізуються чек-боксами, перевіряє, чи обрано правильну відповідь. '''''

    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, showed_answer, result):
        ''' запам'ятовує всі властивості. showed_answer - це віджет, у якому записується правильна відповідь (показується пізніше)
        result - це віджет, у який буде записано txt_right або txt_wrong'''
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result

    def check(self):
        ''' відповідь заноситься в статистику, але перемикання у формі не відбувається: 
        цей клас нічого не знає про панелі на формі '''
        if self.answer.isChecked():
            self.result.setText('Правильно')
            self.showed_answer.setText(self.frm_model.answer)
        else:
            self.result.setText('Не правильно')
            self.showed_answer.setText(self.frm_model.answer)










class QuestionListModel(QAbstractListModel):
    ''' в даних знаходиться список об'єктів типу Question,
    а також список активних запитань, щоб показувати його на екрані '''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = []

    def rowCount(self, index):
        ''' число елементів для показу: обов'язковий метод для моделі, з якою буде пов'язаний віджет "список"'''
        return len(self.form_list)

    def data(self, index, role):
        ''' обов'язковий метод для моделі: які дані вона дає за запитом від інтерфейсу'''
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question

    def insertRows(self, parent=QModelIndex()):
        ''' цей метод викликається, щоб вставити в список об'єктів нові дані;
        генерується і вставляється одне порожнє запитання.'''
        position = len(self.form_list)
        self.beginInsertRows(parent, position, position)
        self.form_list.append(Question())
        self.endInsertRows()
        QModelIndex()
        return True  # повідомляємо, що все пройшло добре

    def removeRows(self, position, parent=QModelIndex()):
        ''' стандартний метод для видалення рядків - після видалення з моделі рядок автоматично видаляється з екрана '''
        self.beginRemoveRows(parent, position, position)
        self.form_list.pop(position)
        self.endRemoveRows()
        return True

    def random_question(self):
        ''' Видає випадкове запитання '''
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]


def random_AnswerCheck(list_model, w_question, widgets_list, w_showed_answer, w_result):
    '''повертає новий екземпляр класу AnswerCheck,
    з випадковим питанням і випадковим розкидом відповідей по віджетах'''
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_card = AnswerCheck(frm, w_question, widgets_list[0], widgets_list[1], widgets_list[2], widgets_list[3], w_showed_answer, w_result)
    return frm_card