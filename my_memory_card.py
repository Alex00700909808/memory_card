#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QRadioButton,QPushButton,QGroupBox,QHBoxLayout,QVBoxLayout,QButtonGroup)
from random import *

class Question():
    def __init__(self, question, right, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right = right
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3


App = QApplication([])
main_win = QWidget()

RadioGroupBox = QGroupBox('Варианты ответов:')

#Кнопки ответов
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#Линии группы
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans4 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

# группа с результатом
RadioGroupBoxRes = QGroupBox('Результат теста')

res_text = QLabel('Верно/Неверно')
answer_text = QLabel('Правильный ответ')

ans_line = QVBoxLayout()

ans_line.addWidget(res_text, alignment=(Qt.AlignCenter))
ans_line.addWidget(answer_text,alignment=(Qt.AlignCenter))
RadioGroupBoxRes.setLayout(ans_line)

lb_Question = QLabel('Какой национальности не существует?')
layout_ans4.addWidget(lb_Question, alignment=(Qt.AlignHCenter))

RadioGroupBox.setLayout(layout_ans1)
layout_ans4.addWidget(RadioGroupBox, alignment=(Qt.AlignHCenter))

layout_ans4.addWidget(RadioGroupBoxRes,alignment=(Qt.AlignHCenter))
btn_OK = QPushButton('Ответить')

layout_ans4.addWidget(btn_OK, stretch=2)

q1 = Question('Как переводится слово "переменная"', 'variable', 'variant', 'variation', 'changing')
q2 = Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Бразилский', 'Английский')
q3 = Question('Сколько континентов на земле', '6', '10', '5', '27')


#Функции
#Показать вопрос
def show_question():
    RadioGroupBox.show()
    RadioGroupBoxRes.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

#Показать результат
def show_result():
    RadioGroupBox.hide()
    RadioGroupBoxRes.show()
    btn_OK.setText('Следущий вопрос')

#Перестановка местами вариантов ответа
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    lb_Question.setText(q.question)
    show_question()

def show_correct(res, correct_ans):
    res_text.setText(res)
    answer_text.setText(correct_ans)

#Проверка ответа
def test():
    if answers[0].isChecked():
        show_correct('Верно', answers[0].text())
        show_result()
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно', answers[0].text())
        show_result()


def next_question():
    n = randint(0, len(questions_list) - 1)
    q = questions_list[n]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        test()
    else:
        next_question()

btn_OK.clicked.connect(click_OK)
RadioGroupBoxRes.hide()
main_win.setLayout(layout_ans4)

main_win.quest_num = -1
questions_list = []
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
next_question()

#Конец программы
main_win.show()
App.exec_()

