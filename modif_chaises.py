import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import glob, os
from projet import Ui_MainWindow
from classes import *
from copy import deepcopy

class Modif(QWidget):

    def __init__(self):
        
        QWidget.__init__(self)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(000, 000, 255))
        point = QPoint(10,10)
        image = QImage("Icons/chaise.jpg");
        painter.drawImage(point, image);
        painter.end()
