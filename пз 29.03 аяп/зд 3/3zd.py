from PyQt5 import QtWidgets, uic
from d4 import Ui_MainWindow
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
            to = self.ui.lnt0.text()
            ts = self.ui.lnts.text()
            k = self.ui.lnk.text()
            if 0 < float(t0) <= 1000 and 0 < float(ts) <= 45 and 0 < float(k) < 1000:
                temp = [ts + (t0 - ts) * math.exp(-k*i) for i in range(0, 100)]
                plt.plot(temp, 100)
                plt.xlabel('температура')
                plt.ylabel('время')
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