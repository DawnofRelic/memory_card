from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
app = QApplication([])
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3  

question_list=[]
question_list.append(Question("koliko je 3 plus 3","6","8","69","0"))
question_list.append(Question("koji je najbolji film?","Shrek","Jaws","Room","It"))
question_list.append(Question("koliko je 66 plus 85?","151","200","67","152"))
question_list.append(Question("Šta je 8. marta?","1 Februar","Dan žena","Obićan dan","Preskoči"))
question_list.append(Question("koliko osoba koja je rođena u 2010 ima sad godina","14","130","68","2"))
question_list.append(Question("koja je najveća planeta u našem S.  sistemu","Jupiter","Mars","Saturn","Venera"))
question_list.append(Question("ko je najbogatiji čovjek na svijetu","Jeff Bezos","Bill Gates","Michael Jackson","Michael Jordan"))
question_list.append(Question("koja je sad trenutno godina","2024","2000","3001","80085"))
question_list.append(Question("Koje je moje ime","Imran","Daris","Muhamed","Anel"))
question_list.append(Question("koji je najbrži čcovjek na svijetu","usain bolt","tvoj komšija","Bill gates","Abdulah abdulaziz"))





my_win = QWidget()
my_win.setWindowTitle("Memory Card")
button = QPushButton("Answer")
text = QLabel("Which nationality does not exist?")
RGB = QGroupBox("Answer options")
btn_1 = QRadioButton("Smurfs")
btn_2 = QRadioButton("Chulyms")
btn_3 = QRadioButton("Enets")
btn_4 = QRadioButton("Aleuts")
RGBb = QButtonGroup()
RGBb.addButton(btn_1)
RGBb.addButton(btn_2)
RGBb.addButton(btn_3)
RGBb.addButton(btn_4)

ans_1 = QVBoxLayout ()
ans_2 = QVBoxLayout ()
ans_3 = QHBoxLayout ()

ans_2.addWidget(btn_1)
ans_2.addWidget(btn_2)
ans_1.addWidget(btn_3)
ans_1.addWidget(btn_4)
ans_3.addLayout(ans_2)
ans_3.addLayout(ans_1)

RGB.setLayout(ans_3)

AnsGroupBox = QGroupBox("Test results")
lb_result = QLabel("Are you correct or not")
In_Correct = QLabel("Smurfs")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop) )
layout_res.addWidget(In_Correct, alignment=Qt.AlignCenter, stretch=2 )

AnsGroupBox.setLayout(layout_res)




hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()
main_line = QVBoxLayout()
hline1.addWidget(text, ( Qt.AlignCenter | Qt.AlignCenter))
hline2.addWidget(RGB)
hline2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

hline3.addStretch(1)
hline3.addWidget(button, stretch = 2)
hline3.addStretch(1)

main_line.addLayout(hline1, stretch= 2)
main_line.addLayout(hline2, stretch= 8)
main_line.addStretch(1)
main_line.addLayout(hline3, stretch= 2)
main_line.addStretch(1)
main_line.addStretch(5)

def show_result():
    RGB.hide()
    AnsGroupBox.show()
    button.setText("Next question")

def show_question():
    AnsGroupBox.hide()
    RGB.show()
    button.setText("Answer")
    RGBb.setExclusive(False)
    btn_1.setChecked(False) 
    btn_1.setChecked(False)
    btn_1.setChecked(False)
    btn_1.setChecked(False)
    RGBb.setExclusive(True)

answers = [btn_1, btn_2, btn_3, btn_4]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1) 
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    In_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer(): 
    if answers[0].isChecked():
        show_correct("Correct")
        my_win.score += 1
        print("Statistics\n-Total answers:", my_win.total, "\nRight answer:", my_win.score)
        print("Rating", (my_win.score/my_win.total*100),"%")
    else:
    
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect")
            print("Rating", (my_win.score/my_win.total*100),"%")
        


def next_question():
    my_win.total += 1
    print("Statistics\n-Total answers:", my_win.total, "\nRight answer:", my_win.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if button.text() == "Answer":
        check_answer()
    else:
        next_question()
 
my_win.setLayout(main_line)
my_win.total = 0
my_win.score = 0
next_question()
button.clicked.connect(click_OK)
my_win.show()
app.exec()

