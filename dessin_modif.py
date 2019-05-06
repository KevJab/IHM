import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import glob, os
from projet import Ui_MainWindow
from classes import *
from copy import deepcopy

class Modif(QWidget):

    def __init__(self, taille_restau, liste_tables, liste_chaises, fenetre):
        
        QWidget.__init__(self)
        self.taille_restau = taille_restau
        self.liste_tables = liste_tables
        self.liste_chaises = liste_chaises
        self.X = 0
        self.Y = 0
        self.fenetre = fenetre
        

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(000, 000, 255))
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        nb_tables = len(self.liste_tables)
        for i in range(nb_tables):
            nb_rect = len(self.liste_tables[i])
            for j in range(nb_rect):
                x, y = self.liste_tables[i][j]
                painter.drawRect(x*10, y*10, 10, 10)

        for chaises in self.liste_chaises:
            x, y = chaises
            painter.drawRect(x*10+2, y*10+2, 6, 6)
        painter.end()

    def mousePressEvent(self, event):
        print("Presser")
        self.X = event.x()
        self.Y = event.y() 
        self.update()

    def mouseReleaseEvent(self, event):
        print("relacher")
        self.fenetre.modifXY(self.X, self.Y)
        self.update()
