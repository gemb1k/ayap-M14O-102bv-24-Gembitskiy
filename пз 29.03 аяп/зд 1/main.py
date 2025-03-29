from PyQt5 import QtWidgets, uic
from test import Ui_MainWindow
import sys
import math
import matplotlib.pyplot as plt


class my_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_win, self).__init__() #наследование атрибутов из QMainWindow
        self.ui = Ui_MainWindow() #cоздание ui
        self.ui.setupUi(self) #создание приложения
        self.ui.btn.clicked.connect(self.btnClicked)

    def btnClicked(self):
        try:
            Vn = self.ui.Vnl.text()
            phin = self.ui.phinl.text()
            if 0 < float(Vn) <= 100 and 0 < float(phin) <= 90:
                Vx = Vn * math.cos(phin)
                Vy = Vn * math.sin(phin)
                tp = 2 * (Vy/9.8)           #время полета
                x = [Vx * i for i in range(tp + 1)]   #создам масив из х а след строчкой из у, коорд тела в люб момент полета
                y = []
                for i in range(0, int(tp // 2)):
                    y.append(Vy * tp - 9.8 * int(tp) **2 // 2)
                y += y[::-1] #добавляем к спискку обратный, это мы имеем право сделать так как коррдинаты при полете вниз повторятьяс
                plt.plot(x, y)
                plt.xlabel('X координата')
                plt.ylabel('Y координата')
                plt.show()
            else:
                txt = 'введите реальные значения'
                self.ui.lblo.setText(txt)
        except ValueError:
            text = "введите числа"
            self.ui.lblo.setText(text)

app = QtWidgets.QApplication([]) #создание приложения
window = my_win()
window.show() #показ окна

sys.exit(app.exec())