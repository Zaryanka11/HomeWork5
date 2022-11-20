import datetime
import sys
import random

from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget): #класс, который наследует функционал от виджетов
    def __init__(self): #наделяем init определённым функционалом
        super().__init__() #рандомим оценки
        self.marks = [
      'All right - 5', #список оценок
            'Good - 4',
            'Baaad - 3',
            'Very baaaaad - 2',
      ]
        self.button = QtWidgets.QPushButton("Get random mark!") #добавление кнопки
        self.label = QtWidgets.QLabel(
            'Random mark maker!',
            alignment=QtCore.Qt.AlignCenter  # настройка центровки
        ) #объект

        self.layout = QtWidgets.QVBoxLayout(self) #шкафчик с полками, куда мы можем добавлять какие-то объекты
        #механизм разделения объектов на gui-шки (как они буду располагаться и что там будет)

        self.layout.addWidget(self.label) #помещаем в панель
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.button_click)


        def button_click(self): #логика для нажатия кнопки
            dt = datetime.datetime.now()
            print(f'Button clicked at {dt}')
            self.label.setText(random.choice(self.marks))


if __name__ == '__main__': #если у нас главный поток - приложение стартует в качестве некоторого скрипта
    app = QtWidgets.QApplication([]) #создаётся некий объект с приложением

    widget = MyWidget() #создаём объект класса нашего виджета
    widget.resize(1000, 800) #задаём размер
    widget.show() #чтобы widget показался

    sys.exit((app.exec())) #остановить сервер