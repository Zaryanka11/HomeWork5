from PyQt5.QtWidgets import * #перенос файлов из библиотеки PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#библиотека sys, чтобы программа закрывалась без ошибок
import sys

#класс для создания приложения и синхронизации с "Главным окном"
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #Функции для определения заголовка и размера проекта
        self.setWindowTitle("Python ") #Задать заголовок окна
        self.setGeometry(100, 100, #Задать геометрию
                         300, 500)
        #Квадратики в функции "Компоненты пользовательского интерфейса"
        self.UiComponents()

        self.show()

    #Квадратики в функции "Компоненты пользовательского интерфейса"
    def UiComponents(self):
        self.turn = 0
        self.times = 0
        self.push_list = []
        #Цикл for используются при создании квадратиков
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            self.push_list.append(temp)
        x = 90
        y = 90
        #Цикл for используются при создании квадратиков
        for i in range(3):
            for j in range(3):
                #Задаём расстрояние между квадратиками
                self.push_list[i][j].setGeometry(x * i + 20,
                                                 y * j + 20,
                                                 80, 80)
                #Задаём размер букв "О" и "Х"
                self.push_list[i][j].setFont(QFont(QFont('Times', 35)))
                #Что произойдёт при нажатии на квадратик
                self.push_list[i][j].clicked.connect(self.action_called)
        #Создана "Метка", чтобы указать, кто победит(или ничья)
        self.label = QLabel(self)
        #Физические свойства объекта "Метка" определяются в функциях
        self.label.setGeometry(20, 300, 260, 60) #Установить геометрию

        self.label.setStyleSheet("QLabel" #установить стиль
                                 "{"
                                 "border : 3px solid black;"
                                 "background : green;"
                                 "}")

        self.label.setAlignment(Qt.AlignCenter) #установить выравнивание

        self.label.setFont(QFont('Times', 15)) #установить шрифт

        reset_game = QPushButton("Reset-Game", self)
        #Когда игра заканчивается, создаётся кнопка для перезапуска
        reset_game.setGeometry(50, 380, 200, 50)
        #Что произойдёт при нажатии на кнопку перезапуска (игра сбросится)
        reset_game.clicked.connect(self.reset_game_action)
        #Функция для сброса игры
    def reset_game_action(self):

        self.turn = 0
        self.times = 0

        self.label.setText("")

        for buttons in self.push_list:
            for button in buttons:
                button.setEnabled(True)
                button.setText("")
    #Функция для определения работы букв "О" и "Х"
    def action_called(self):

        self.times += 1
        button = self.sender()
        button.setEnabled(False)
        #Структура запроса if и else используются, чтобы буквы "О" и "Х" менялись
        if self.turn == 0:
            button.setText("X")
            self.turn = 1
        else:
            button.setText("O")
            self.turn = 0
         #Функция "кто победил" создана, чтобы проверить, закончилась ли игра
        win = self.who_wins()
        text = ""

        if win == True:
            if self.turn == 0:
                #По результату функции в объекте "метка" отображается, кто выиграл игру
                text = "O Won"
            else:
                text = "X Won"

            for buttons in self.push_list:
                for push in buttons:
                    push.setEnabled(False)
        #Если игра не закончилась за 0 ходов, в объекте "Метка" пишет, что игра закончилась ничьей
        elif self.times == 9:
            text = "Match is Draw"

        self.label.setText(text)
    #В функции "кто победил" каждый раз проверяется, закончилась игра или нет
    def who_wins(self):
        for i in range(3):
            if self.push_list[0][i].text() == self.push_list[1][i].text() \
                    and self.push_list[0][i].text() == self.push_list[2][i].text() \
                    and self.push_list[0][i].text() != "":
                return True

        for i in range(3):
            if self.push_list[i][0].text() == self.push_list[i][1].text() \
                    and self.push_list[i][0].text() == self.push_list[i][2].text() \
                    and self.push_list[i][0].text() != "":
                return True
        #Запрос "если" используется для контрольных операций
        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != "":
            return True
        #Запрос "если" используется для контрольных операций
        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[1][1].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != "":
            return True

        return False
#Создаётся переменная и синхронизируется с объектом, созданным с аргументом Sys
App = QApplication(sys.argv)
#Синхронизировалась переменная с классом, созданным в начале кода
window = Window()
#При нажатии кнопки закрытия приложение закрывается без ошибок
sys.exit(App.exec())