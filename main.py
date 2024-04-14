from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QWidget, QGroupBox, QRadioButton)
from random import shuffle

class Question:
    def __init__(self, question, correct_ans, wrongans1, wrongans2, wrongans3):
        self.question = question
        self.correct_ans = correct_ans
        self.wrong_ans1 = wrongans1
        self.wrong_ans2 = wrongans2
        self.wrong_ans3 = wrongans3

app = QApplication([])
window = QWidget()
window.setWindowTitle('ქვიზი')

btn_submit = QPushButton('პასუხი')
question = QLabel('როდის შეიქმნა პროგრამირების ენა პითონი?')

radio_group = QGroupBox('სავარაუდო პასუხები:')
ans1 = QRadioButton('1993')
ans2 = QRadioButton('2003')
ans3 = QRadioButton('1991')
ans4 = QRadioButton('2001')

lt_ans1 = QHBoxLayout()
lt_ans2 = QVBoxLayout()
lt_ans3 = QVBoxLayout()

lt_ans2.addWidget(ans1)
lt_ans2.addWidget(ans2)
lt_ans3.addWidget(ans3)
lt_ans3.addWidget(ans4)

lt_ans1.addLayout(lt_ans2)
lt_ans1.addLayout(lt_ans3)

radio_group.setLayout(lt_ans1)

layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()

layout_l1.addWidget(question, alignment=Qt.AlignHCenter)
layout_l2.addWidget(radio_group)
layout_l2.setSpacing(10)
layout_l3.addStretch(4)
layout_l3.addWidget(btn_submit, alignment=Qt.AlignHCenter, stretch=5)
layout_l3.addStretch(4)
layout_l3.setSpacing(10)

layout = QVBoxLayout()
layout.addLayout(layout_l1)
layout.addLayout(layout_l2)
layout.addLayout(layout_l3)

ans_groupbox = QGroupBox('ტესტის შედეგები:')
result_label = QLabel('სწორი ხარ თუ არა?')
correct_ans = QLabel('სწორი პასუხია:')

layout_res = QVBoxLayout()
layout_res.addWidget(result_label, alignment=(Qt.AlignHCenter | Qt.AlignTop))
# layout_res.addWidget(correct_ans, alignment=(Qt.AlignHCenter | Qt.AlignBottom))
ans_groupbox.setLayout(layout_res)

# layout_l1.addWidget(layout_res, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_l2.addWidget(ans_groupbox)
ans_groupbox.hide()


def show_result():
    radio_group.hide()
    ans_groupbox.show()
    btn_submit.setText('შემდეგი კითხვა')


def show_question():
    ans_groupbox.hide()
    radio_group.show()
    btn_submit.setText('პასუხი')
    radio_group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    radio_group.setExclusive(True)



answers = [ans1, ans2, ans3, ans4]


def ask(q: Question):
    shuffle(answers)
    answers[2].setText(q.correct_ans)
    answers[3].setText(q.wrong_ans1)
    answers[0].setText(q.wrong_ans2)
    answers[1].setText(q.wrong_ans3)
    question.setText(q..question)
    correct_ans.setText(q.correct_ans)
    show_question()

    def show_correct(res)
        result_label.setText(res)
        correct_ans.show()

        def check_answer():
            if answers[2].isChecked():
                show_correct("სწორია!")
            else:
                if answers[0].isChecked() or answers[1].isChecked() or answers[3]isChecked().
                show_correct("არასწორია!")


window.setLayout(layout)
window.resize(800, 600)
btn_submit.clicked.connect(test)
window.show()
app.exec_()
