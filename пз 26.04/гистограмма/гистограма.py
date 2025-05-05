from PyQt5 import QtWidgets, uic
from gist import Ui_MainWindow
import sys
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class my_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_win, self).__init__() #наследование атрибутов из QMainWindow
        self.ui = Ui_MainWindow() #cоздание ui
        self.ui.setupUi(self) #создание приложения
        self.ui.pdtstr.clicked.connect(self.pdtstrClicked)
        self.ui.pbtgen.clicked.connect(self.pbtgenClicked)

        #блок чтоюбы подружить матплотлиб и пайкут:
        self.figure = Figure(figsize=(8, 5))
        self.canvas = FigureCanvas(self.figure)

        scene = QtWidgets.QGraphicsScene()
        scene.addWidget(self.canvas)
        self.ui.gr.setScene(scene)

    def pdtstrClicked(self):
        try:
            self.tocki = [int(x) for x in self.ui.numbers.text().split()]
            self.figure.clear()
            ax = self.figure.add_subplot(111)

            ax.hist(self.tocki, bins=10, color='red', edgecolor='black')
            ax.set_title('Гистограмма значений', fontsize=12)
            ax.set_xlabel('Значение', fontsize=10)
            ax.set_ylabel('Частота появления', fontsize=10)

            self.canvas.draw()
            self.ui.znach.setText("")

        except ValueError:
            self.ui.znach.setText("Ошибка: введите числа через пробел или запятую!")

    def pbtgenClicked(self):
        self.random_numbers = [random.randint(1, 100) for _ in range(10)]

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.hist(self.random_numbers, bins=10, color='red', edgecolor='black')
        ax.set_title('Гистограмма значений', fontsize=12)
        ax.set_xlabel('Значение', fontsize=10)
        ax.set_ylabel('Частота появления', fontsize=10)

        self.canvas.draw()
        self.ui.znach.setText("")


app = QtWidgets.QApplication([]) #создание приложения
window = my_win()
window.show() #показ окна

sys.exit(app.exec())