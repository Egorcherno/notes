#тут могла быть ваша реклама
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

test={
    'дз на 7 декабря':'cтраница 156 параграф 3',
    'текст заметки':'ntrcn',
    "FFFFFFFF":"памагите меня тут держат в заложниках"
}

#with open('basa.json','w',encoding='utf-8') as file:
#    json.dump(test,file,ensure_ascii=False)

with open('basa.json','r',encoding='utf-8') as file:
    test = json.load(file)
app=QApplication([])
window = QWidget()

m_l = QHBoxLayout()
m_l1 = QHBoxLayout()
m_l2 = QHBoxLayout()
mm2=QVBoxLayout()

sz = QLabel("Список заметок")
n_l = QListWidget()
editer = QTextEdit()
st = QLabel('Список тегов')
t_l = QListWidget()
f = QLineEdit('Введи')

knopka = QPushButton("Схранить текст")
knopka1 = QPushButton("Создать заметку")
knopka2= QPushButton("Удалить заматку")
knopka4 = QPushButton("Создать тег")
knopka5 = QPushButton("Удалить тег")
knopka6 = QPushButton("Искать по тегу")



m_l.addWidget(editer)

mm2.addWidget(sz)
mm2.addWidget(n_l)
mm2.addLayout(m_l1)

mm2.addWidget(knopka)
m_l1.addWidget(knopka1)
m_l1.addWidget(knopka2)

mm2.addWidget(st)
mm2.addWidget(t_l)
mm2.addWidget(f)
mm2.addLayout(m_l2)
m_l2.addWidget(knopka4)
m_l2.addWidget(knopka5)

mm2.addWidget(knopka6)
n_l.addItems(test)
def show_n():
    key = n_l.selectedItems()[0].text()
    s = test[key]
    editer.setText(s)


def save():
    key = n_l.selectedItems()[0].text()
    test[key] = editer.toPlainText()
    n_l.clear()
    n_l.addItems(test)
    with open('basa.json','w',encoding='utf-8') as file:
        json.dump(test,file,ensure_ascii=False)

def crate ():
    dil = QInputDialog.getText(window,'Добавить заметку','название заметки')
    dil= dil[0]
    test[dil]=editer.toPlainText() 
    n_l.clear()
    n_l.addItems(test)
    with open('basa.json','w',encoding='utf-8') as file:
        json.dump(test,file,ensure_ascii=False)
def delete ():
    key = n_l.selectedItems()[0].text()
    del test[key]
    n_l.clear()
    n_l.addItems(test)

    with open('basa.json','w',encoding='utf-8') as file:
        json.dump(test,file,ensure_ascii=False)
m_l.addLayout(mm2)
window.setLayout(m_l)

n_l.itemClicked.connect(show_n)
knopka.clicked.connect(save)
knopka1.clicked.connect(crate)
knopka2.clicked.connect(delete)
window.show()
app.exec()