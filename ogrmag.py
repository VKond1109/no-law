from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QButtonGroup, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle,randint
 
app = QApplication([])
 
 
window = QWidget()
window.setWindowTitle('Memo Card')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2 
        self.wrong3 = wrong3


questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
 
'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('В каком году была основана Москва?') 
 
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('9')
rbtn_2 = QRadioButton('10')
rbtn_3 = QRadioButton('11')
rbtn_4 = QRadioButton('12')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


 
layout_ans1 = QHBoxLayout()     
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
 
RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox('Результат теста') 
lb_result = QLabel('прав или нет')
lb_correct = QLabel('ответ будет тут')

Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_result,alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter, stretch =2)
AnsGroupBox.setLayout(Layout_res)

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout()



 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout()
 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
 

layout_card = QVBoxLayout()
 
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 
 
def show_result():
     RadioGroupBox.hide()
     AnsGroupBox.show()
     btn_OK.setText('Следуйщий вопрос')

def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
   
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
 
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) 
    lb_correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score +=1
        print('стистика\n - Всего вопросов:', window.total,'n\-Правильных ответов:', window.total)
        print('Рейтинг:',(window.score/window.total*100,'%'))
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:',(window.score/window.total*100,'%'))
 
def next_question():
    window.total +=1
    print('стистика\n - Всего вопросов:', window.total,'n\-Правильных ответов:', window.total)
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q) 

def click_OK():
    
    if btn_OK.text() == 'Ответить':
        check_answer() 
    else:
        next_question() 

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.total = 0
window.score = 0
 
btn_OK.clicked.connect(click_OK) 
 
next_question()
window.resize(400, 300)
window.show()
app.exec()
