import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import glob, os
from projet import Ui_MainWindow
from classes import *
from copy import deepcopy
import dessin
import modif_chaises
import dessin_modif


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.commande = Commande(None, None, None, None)
        """
        COMMANDE POUR TEST
        """
        frite = Plat("Frite",1,[patate],[],"",[])
        kebab = Plat("Kebab",6,[viande,salade,tomate,oignon],[],"",[frite])
        poulet = Plat("Poulet",1,[],[],"",[])
        crevette = Plat("Crevette",1,[],[],"",[])
        coca = Boisson("Coca",1,[],[],"",False,25)
        pepsi = Boisson("Pepsi",1,[],[],"",False,25)
        
        m = Menu("Kebab_Frites",[kebab, frite],coca,6.5)
        self.taille_restau = [30, 30]
        self.liste_tables = [[(1,1),(2,1),(1,2),(2,2)], [(5,5),(5,6),(5,7),(6,5),(6,6),(6,7)]]
        self.liste_chaises = [(0,1),(0,2),(3,1),(3,2),(5,4),(6,4),(4,5),(4,6),(4,7),(7,5),(7,6),(7,7),(5,8),(6,8)]
        self.X = 0
        self.Y = 0
        self.dessin = None
        self.obj2 = QVBoxLayout()
        self.formTables = None
        self.commande = Commande([m], [poulet, crevette], [pepsi], None)  # Commande pour tester
        self.all_commandes = [self.commande, deepcopy(self.commande), deepcopy(self.commande)]
        self.vue = "Modif_Tables"
        super(MainWindow, self).__init__()
        self.setupUi(self)

        if(self.vue == "Commande"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QVBoxLayout(frame)
            self.textEdit = QTextEdit(self)
            self.textEdit.setContentsMargins(0,0,0,0)
            s = ""
            total = 0

            s += "Boissons \n ----------------------------------\n"
            if self.commande.boissons:
                for n in self.commande.boissons:
                    s+= n.nom + "\t\t\t" + str(n.prix) + "€\n"
                    total += n.prix
            s += "\n\nPlats \n ----------------------------------\n"
            if self.commande.plats:
                for m in self.commande.plats:
                    s += m.nom + "\t\t\t" + str(m.prix) + "€\n"
                    total += m.prix
            s += "\n\nMenus \n ----------------------------------\n"
            if self.commande.menus:
                for o in self.commande.menus:
                    s += o.nom + "\t\t\t" + str(o.prix) + "€\n"
                    total += o.prix

            s += "\n\n\n\nTotal \n -------------------------------------------------------------------\n\t\t\t" + str(total) + "€"

            self.textEdit.setText(s)
            self.textEdit.adjustSize()
            btn = QPushButton('Payer', self)
            btn.resize(50, 50)
            btn.setStyleSheet("background-color: yellow;")
            obj.addWidget(self.textEdit)
            obj.addWidget(btn)

        if(self.vue == "All_Commande"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QHBoxLayout(frame)


            for k in self.all_commandes:
                obj2 = QVBoxLayout()
                self.textEdit = QTextEdit(self)
                self.textEdit.setContentsMargins(0,0,0,0)
                s = ""
                if k.menus:  # Je rassemble tous les plats et les boissons pour que ce soit plus lisible
                    for i in k.menus:
                        for j in i.plats:
                            k.plats.append(j)
                        k.boissons.append(i.boisson)
                s += "Boissons \n ----------------------------------\n"
                if k.boissons:
                    for n in k.boissons:
                        s+= n.nom + "\n"
                s += "\n\nPlats \n ----------------------------------\n"
                if k.plats:
                    for m in k.plats:
                        s += m.nom + "\n"
                self.textEdit.setText(s)
                self.textEdit.adjustSize()
                btn = QPushButton('Terminer', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: red;")
                obj2.addWidget(self.textEdit)
                obj2.addWidget(btn)
                obj.addLayout(obj2)

            #TODO enlever la commande quand le bouton "Terminer" est appuyé

        elif(self.vue == "Plats"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QVBoxLayout(frame)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Plat_*.txt')):
                f = open(txt_file, "r")
                txt = f.readlines()
                t = QTextEdit(self)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                t.setPlainText(''.join(map(str, txt)))
                obj.addWidget(t)
                obj.addWidget(btn)

                #TODO quand le bouton est push ajouter le plat à la commande (self.commande)

        elif(self.vue == "Boissons"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QVBoxLayout(frame)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Boisson_*.txt')):
                f = open(txt_file, "r")
                txt = f.readlines()
                t = QTextEdit(self)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                t.setPlainText(''.join(map(str, txt)))
                obj.addWidget(t)
                obj.addWidget(btn)

                #TODO quand le bouton est push ajouter la boisson à la commande (self.commande)

        elif(self.vue == "Menus"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QVBoxLayout(frame)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Menu_*.txt')):
                f = open(txt_file, "r")
                txt = f.readlines()
                t = QTextEdit(self)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                t.setPlainText(''.join(map(str, txt)))
                obj.addWidget(t)
                obj.addWidget(btn)

                #TODO quand le bouton est push ajouter le menu à la commande (self.commande)

        elif(self.vue == "Tables"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QHBoxLayout(frame)
            obj2 = QVBoxLayout()
            dess = dessin.Dessin(self.taille_restau, self.liste_tables, self.liste_chaises)
            obj2.addWidget(dess)
            obj.addLayout(obj2)

        elif(self.vue == "Modif_Tables"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QHBoxLayout(frame)
            grid = QGridLayout()
            modifchaises = modif_chaises.Modif()
            grid.addWidget(modifchaises,0,0)
            bouttonPlus = QPushButton("+")
            bouttonPlus.resize(100,32)
            grid.addWidget(bouttonPlus,0,1)
            bouttonPlus.clicked.connect(self.ajouterChaises)
            bouttonMoins = QPushButton("-")
            bouttonMoins.resize(100,32)
            grid.addWidget(bouttonMoins,0,2)
            bouttonMoins.clicked.connect(self.retirerChaises)
            #partie pour les tables
            Nomtables = QLabel("Nombre de tables:")
            Nomtables.setAlignment(Qt.AlignCenter)
            grid.addWidget(Nomtables, 1, 0, 1, 2)
            self.formTables = QSpinBox()
            grid.addWidget(self.formTables, 1, 2)
            self.formTables.valueChanged.connect(self.modifTables)
            self.obj2.addLayout(grid)
            self.dessin = dessin_modif.Modif(self.taille_restau, self.liste_tables, self.liste_chaises, self)
            self.obj2.addWidget(self.dessin)
            obj.addLayout(self.obj2)

    def modifTables(self):
        nbTables = self.formTables.value()
        table = self.trouverTable()
        tab = []
        if table == None and nbTables%2 == 0:
            a = self.X//10
            b = self.Y//10
            for i in range(0, 2):
                for j in range(0, nbTables//2):
                    tab.append((i+a, j+b))

        if len(tab) > 0:
            self.liste_tables.append(tab)
            
            self.dessin.deleteLater()
            self.dessin = dessin_modif.Modif(self.taille_restau, self.liste_tables, self.liste_chaises, self)
            self.obj2.addWidget(self.dessin)


    def ajouterChaises(self):
        table = self.trouverTable()
        a, b = table[0]
        c, d = table[len(table)-1]
        ajouter = False
        print("liste")
        print(self.liste_chaises)
        print("okay")
        print(c-a)
        for i in range(0, c-a+1):
            trouver1 = False
            trouver2 = False
            for j in range(len(self.liste_chaises)):
                r, s = self.liste_chaises[j]
                if (r == i+a and s == b-1) and not(ajouter):
                    trouver1 = True

                if (r == i+a and s == d+1) and not(ajouter):
                    trouver2 = True
            if not(trouver1) and not(ajouter):
                self.liste_chaises.append((i+a, b-1))
                ajouter = True

            if not(trouver2) and not(ajouter):
                self.liste_chaises.append((i+a, d+1))
                ajouter = True
                  
        for i in range(0, d-b+1):
            trouver1 = False
            trouver2 = False
            for j in range(len(self.liste_chaises)):
                r, s = self.liste_chaises[j]
                if (r == a-1 and s == i+b) and not(ajouter):
                    trouver1 = True

                if (r == c+1 and s == i+b) and not(ajouter):
                    trouver2 = True

            if not(trouver1) and not(ajouter): 
                self.liste_chaises.append((a-1, i+b))
                ajouter = True
            
            if not(trouver2) and not(ajouter):
                self.liste_chaises.append((c+1, i+b))
                ajouter = True
                
        self.dessin.deleteLater()
        self.dessin = dessin_modif.Modif(self.taille_restau, self.liste_tables, self.liste_chaises, self)
        self.obj2.addWidget(self.dessin)


    def retirerChaises(self):
        table = self.trouverTable()
        a, b = table[0]
        c, d = table[len(table)-1]
        retirer = False
        print("liste")
        print(self.liste_chaises)
        for i in range(0, c-a+1):
            for j in range(len(self.liste_chaises)):
                r, s = self.liste_chaises[j]
                if (r == i+a and s == b-1) and not(retirer):
                    self.liste_chaises.remove((i+a, b-1))
                    retirer = True
                    break

                if (r == i+a and s == d+1) and not(retirer):
                    self.liste_chaises.remove((i+a, d+1))
                    retirer = True
                    break

        for i in range(0, d-b+1):
            for j in range(len(self.liste_chaises)):
                r, s = self.liste_chaises[j]
                print("okay2")
                print(r)
                print(s)
                print(i+b)
                print(a-1)
                print(c+1)
                if (r == a-1 and s == i+b) and not(retirer):
                    self.liste_chaises.remove((a-1, i+b))
                    retirer = True
                    break

                if (r == c+1 and s == i+b) and not(retirer):
                    self.liste_chaises.remove((c+1, i+b))
                    retirer = True
                    break
                
        self.dessin.deleteLater()
        self.dessin = dessin_modif.Modif(self.taille_restau, self.liste_tables, self.liste_chaises, self)
        self.obj2.addWidget(self.dessin)

    def modifXY(self, x, y):
        self.X = x
        self.Y = y
        print("XY")
        print(self.X)
        print(self.Y)
        print(self.trouverTable())

    def trouverTable(self):
        nb_tables = len(self.liste_tables)
        for i in range(nb_tables):
            nb_rect = len(self.liste_tables[i])
            a, b = self.liste_tables[i][0]
            c, d = self.liste_tables[i][nb_rect-1]
            if self.X >= a*10 and self.X <= (c+1)*10 and self.Y >= b*10 and self.Y <= (d+1)*10:
                return self.liste_tables[i]


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
