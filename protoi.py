from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel
import sys

app = QApplication(sys.argv)
print(app.font())
print('metrix')
print(app.fontMetrics())
mains = QWidget()

btnpush = QPushButton('Push me')
btnshve = QPushButton('And then just shove me')
label = QLabel('')

buttons = QHBoxLayout()
name = QLineEdit()

btnpush.clicked.connect(lambda btndata: print(btndata))
btnpush.clicked.connect(lambda: label.setText('SATISFACTION'))


buttons.addWidget(btnpush)
buttons.addWidget(btnshve)

layout = QVBoxLayout()
layout.addWidget(name)
layout.addLayout(buttons)
layout.addWidget(label)


mains.setLayout(layout)

mains.show()
app.exec()