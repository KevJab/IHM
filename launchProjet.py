import sys

from PyQt5.QtWidgets import *
import glob, os
from projet import Ui_MainWindow
from classes import *
from copy import deepcopy
import dessin

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
        self.commande = Commande([m], [poulet, crevette], [pepsi], None)  # Commande pour tester
        self.all_commandes = [self.commande, deepcopy(self.commande), deepcopy(self.commande)]
        self.vue = "Tables"
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

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
