import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QListWidget,QWidget,QVBoxLayout,QTextEdit,QHBoxLayout,QFrame
import glob, os
from projet import Ui_MainWindow
from classes import *
class MainWindow(QMainWindow, Ui_MainWindow):
    vue = "Plats"
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        if(self.vue == "Commande"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            if(frame!=None):
                print("Trouvé")
            else:
                print("Pas Trouvé")

            
            obj = QHBoxLayout(frame)

            self.commande = []
            c = Commande(0)
            c.addPlatByName("Kebab")
            c.addPlatByName("Frite")
            c.saveCommande()
            c1 = Commande(1)
            c1.addPlatByName("Kebab")
            c1.addBoissonByName("Coca")
            c1.addPlatByName("Frite")
            c1.saveCommande()
            self.commande.append(c)
            self.commande.append(c1)
            print("Comm 2 : "+str(len(self.commande[0].boissons)))
            nb_comm = min(8,len(self.commande))
            #nb_comm = 8

            for i in range(0,nb_comm):    
                frm = QWidget(self)  
                vboxLay = QVBoxLayout(frm)


                self.numeroTable = QTextEdit( self )
                self.numeroTable.setPlainText("Table : "+str(self.commande[i].table))
                self.numeroTable.adjustSize()
                vboxLay.addWidget( self.numeroTable )
                for j in self.commande[i].menus:
                    self.plat = QTextEdit( self )
                    self.plat.setPlainText("Menus : "+str(j.nom)+" : "+str(self.commande[i].table))
                    self.plat.adjustSize()
                    vboxLay.addWidget( self.plat )
                for j in self.commande[i].plats:
                    self.plat = QTextEdit( self )
                    self.plat.setPlainText("Plat : "+str(j.nom)+" : "+str(self.commande[i].table))
                    self.plat.adjustSize()
                    vboxLay.addWidget( self.plat )
                for j in self.commande[i].boissons:
                    self.plat = QTextEdit( self )
                    self.plat.setPlainText("Boisson : "+str(j.nom)+" : "+str(self.commande[i].table))
                    self.plat.adjustSize()
                    vboxLay.addWidget( self.plat )
                obj.addWidget(frm)


            
        elif(self.vue == "Plats"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)     
            obj = QVBoxLayout(frame)

            container = QWidget(self) 
            hLay = QHBoxLayout(container)      
            plats = getPlats()
            for p in plats:
                t = QTextEdit(self)
                t.setPlainText(p.nom)
                hLay.addWidget(t)
            obj.addWidget(container)

            container = QWidget(self) 
            hLay = QHBoxLayout(container)    
            menus = getMenus()
            for p in menus:
                t = QTextEdit(self)
                t.setPlainText(p.nom)
                obj.addWidget(t)
            obj.addWidget(container)

            container = QWidget(self) 
            hLay = QHBoxLayout(container)    
            boissons = getBoissons()
            for p in boissons:
                t = QTextEdit(self)
                t.setPlainText(p.nom)
                obj.addWidget(t)
            obj.addWidget(container)



def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

