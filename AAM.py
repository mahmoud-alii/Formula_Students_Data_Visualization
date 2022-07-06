from PyQt5 import QtWidgets
from AAM_GUI import Ui_MainWindow
import serial
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def speedChange():
    # ui.dial.setValue(ui.horizontalSlider.value())
    # ui.lcdNumber.display(ui.horizontalSlider.value())
    Arduino.reset_input_buffer()
    b = Arduino.readline()
    ui.dial.setValue(int(b.decode()))
    ui.lcdNumber.display(int(b.decode()))


def fuelChange():
    ui.dial_2.setValue(ui.horizontalSlider_2.value())
    ui.progressBar.setValue(ui.horizontalSlider_2.value())

try:
    Arduino = serial.Serial('COM3', 9600)
except Exception:
    print("Error")
else:
    speedChange()
ui.pushButton.clicked.connect(speedChange)


# Arduino.close()
# Arduino.open()
# Arduino.flush()
# Arduino.reset_input_buffer()
# Un-comment one of the following:

# 1 - Infinite loop

# while(Arduino.is_open):
#     b = Arduino.readline()
#     speedChange()
#     ui.dial.valueChanged.connect(speedChange)
#     n = int(b.decode())
#     print(n)
#     Arduino.close()
#     Arduino.open()

# 2 - No Update

# speedChange()
# ui.dial.setValue(int(Arduino.readline().decode()))
# ui.lcdNumber.display(int(Arduino.readline().decode()))
# ui.pushButton.clicked.connect(speedChange)
# n = int(b.decode())
# print(n)


ui.horizontalSlider_2.valueChanged.connect(fuelChange)
ui.dial_2.valueChanged.connect(fuelChange)

sys.exit(app.exec_())
