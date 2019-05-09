import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import glob, os
from projet import Ui_MainWindow
from classes import *
from copy import deepcopy

class Dessin(QWidget):

    def __init__(self, taille_restau, liste_tables, liste_chaises):
        
        QWidget.__init__(self)
        self.taille_restau = taille_restau
        self.liste_tables = liste_tables
        self.liste_chaises = liste_chaises

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(000, 000, 255))
        
        nb_tables = len(self.liste_tables)
        print("nb_tables")
        print(nb_tables)
        for i in range(nb_tables):
            nb_rect = len(self.liste_tables[i])
            print("nb_rect")
            print(nb_rect)
            for j in range(nb_rect):
                x, y = self.liste_tables[i][j]
                print(x)
                print(y)
                painter.drawRect(x*10, y*10, 10, 10)

        for chaises in self.liste_chaises:
            x, y = chaises
            painter.drawRect(x*10+2, y*10+2, 6, 6)
        painter.end()
