from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100,
                         300, 500)
        self.UiComponents()
        self.show()


    def UiComponents(self):
        self.turn = 0
        self.times = 0
        self.push_list = []

        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            self.push_list.append(temp)
        x = 90
        y = 90
        for i in range(3):
            for j in range(3):
                self.push_list[i][j].setGeometry(x * i + 20,
                                                 y * j + 20,
                                                 80, 80)
                self.push_list[i][j].setFont(QFont(QFont('Times', 35)))
                self.push_list[i][j].clicked.connect(self.action_called)


        self.label = QLabel(self)

        self.label.setGeometry(20, 300, 260, 60)

        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : green;"
                                 "}")

        self.label.setAlignment(Qt.AlignCenter)

        self.label.setFont(QFont('Times', 15))

        reset_game = QPushButton("Reset-Game", self)

        reset_game.setGeometry(50, 380, 200, 50)

        reset_game.clicked.connect(self.reset_game_action)

    def reset_game_action(self):

        self.turn = 0
        self.times = 0

        self.label.setText("")

        for buttons in self.push_list:
            for button in buttons:
                button.setEnabled(True)
                button.setText("")

    def action_called(self):

        self.times += 1
        button = self.sender()
        button.setEnabled(False)
        if self.turn == 0:
            button.setText("X")
            self.turn = 1
        else:
            button.setText("O")
            self.turn = 0

        win = self.who_wins()
        text = ""

        if win == True:
            if self.turn == 0:
                text = "O Won"
            else:
                text = "X Won"

            for buttons in self.push_list:
                for push in buttons:
                    push.setEnabled(False)

        elif self.times == 9:
            text = "Match is Draw"

        self.label.setText(text)

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

        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != "":
            return True

        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[1][1].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != "":
            return True

        return False


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())