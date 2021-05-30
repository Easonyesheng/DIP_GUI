import sys

from windows.ImageInput import picture
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QtWidgets.QApplication(sys.argv)
my = picture()
my.show()


sys.exit(app.exec_())