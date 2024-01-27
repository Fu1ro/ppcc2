from PyQt5.QtCore import Qt
import os
from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, \
    QHBoxLayout, QVBoxLayout, QFormLayout, QFileDialog

app = QApplication([])
win = QWidget()
win.setWindowTitle('Easy Editor')
btn_dir = QPushButton("Папка")
lb_image = QLabel("Картинка")
lm_files = QListWidget()
win.resize(700, 500)

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")


row = QHBoxLayout()
col1 = QVBoxLayout()
col2 =QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lm_files)
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setLayout(row)
win.show()
workdir = ''
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    try:
       filenames = filter(os.listdir(workdir), extensions)
       lm_files.clear()
       for filename in  filenames:
           lm_files.addItem(filename)
    except FileNotFoundError as err:
        print(err)


btn_dir.clicked.connect(showFilenamesList)
app.exec_()