# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.frameHome = QtWidgets.QFrame(self.centralwidget)
        self.frameHome.setEnabled(False)
        self.frameHome.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.frameHome.setAutoFillBackground(False)
        self.frameHome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHome.setObjectName("frameHome")
        self.frameMenuRightBar = QtWidgets.QFrame(self.frameHome)
        self.frameMenuRightBar.setGeometry(QtCore.QRect(829, 75, 171, 725))
        self.frameMenuRightBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMenuRightBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMenuRightBar.setObjectName("frameMenuRightBar")
        self.toCommandes = QtWidgets.QPushButton(self.frameMenuRightBar)
        self.toCommandes.setEnabled(False)
        self.toCommandes.setGeometry(QtCore.QRect(10, 10, 151, 91))
        self.toCommandes.setObjectName("toCommandes")
        self.toGestionCarte = QtWidgets.QPushButton(self.frameMenuRightBar)
        self.toGestionCarte.setGeometry(QtCore.QRect(10, 280, 151, 91))
        self.toGestionCarte.setObjectName("toGestionCarte")
        self.toGestionSalle = QtWidgets.QPushButton(self.frameMenuRightBar)
        self.toGestionSalle.setGeometry(QtCore.QRect(10, 600, 151, 91))
        self.toGestionSalle.setObjectName("toGestionSalle")
        self.frameSalle = QtWidgets.QFrame(self.frameHome)
        self.frameSalle.setGeometry(QtCore.QRect(0, 75, 831, 725))
        self.frameSalle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSalle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSalle.setObjectName("frameSalle")
        self.frameTopOptions = QtWidgets.QFrame(self.frameHome)
        self.frameTopOptions.setGeometry(QtCore.QRect(0, 0, 1000, 75))
        self.frameTopOptions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTopOptions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTopOptions.setObjectName("frameTopOptions")
        self.frameCommandes = QtWidgets.QFrame(self.centralwidget)
        self.frameCommandes.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.frameCommandes.setAutoFillBackground(False)
        self.frameCommandes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCommandes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCommandes.setObjectName("frameCommandes")
        self.frameTopOptions_Commandes = QtWidgets.QFrame(self.frameCommandes)
        self.frameTopOptions_Commandes.setGeometry(QtCore.QRect(0, 0, 1000, 75))
        self.frameTopOptions_Commandes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTopOptions_Commandes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTopOptions_Commandes.setObjectName("frameTopOptions_Commandes")
        self.frameGestionCommande = QtWidgets.QFrame(self.frameCommandes)
        self.frameGestionCommande.setGeometry(QtCore.QRect(0, 75, 1000, 725))
        self.frameGestionCommande.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameGestionCommande.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameGestionCommande.setObjectName("frameGestionCommande")
        self.frameCommandesPretes = QtWidgets.QFrame(self.frameGestionCommande)
        self.frameCommandesPretes.setGeometry(QtCore.QRect(0, 0, 100, 725))
        self.frameCommandesPretes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCommandesPretes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCommandesPretes.setObjectName("frameCommandesPretes")
        self.frameVueCommandes = QtWidgets.QFrame(self.frameGestionCommande)
        self.frameVueCommandes.setGeometry(QtCore.QRect(100, 0, 900, 725))
        self.frameVueCommandes.setAutoFillBackground(True)
        self.frameVueCommandes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameVueCommandes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameVueCommandes.setObjectName("frameVueCommandes")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toCommandes.setText(_translate("MainWindow", "Commandes"))
        self.toGestionCarte.setText(_translate("MainWindow", "Gestion de la carte"))
        self.toGestionSalle.setText(_translate("MainWindow", "Gestion de la salle"))

