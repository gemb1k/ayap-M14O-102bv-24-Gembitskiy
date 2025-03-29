from PyQt5 import QtWidgets, uic
from d3 import Ui_MainWindow
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
            a = self.ui.lna.text()
            f = self.ui.lnf.text()
            phi = self.ui.lnphi.text()
            if 0 < float(a) <= 100 and 0 < float(phi) <= 90 and 0 < float(f) < 1000:
                w = 2 * math.pi * f
                t = 100 #его нет в задание так что пусть будет такое
                x = [a * math.sin(w*i + phi) for i in range(t+1)] #масив исков
                plt.plot(t, x)
                plt.xlabel('X координата')
                plt.ylabel('t координата')
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