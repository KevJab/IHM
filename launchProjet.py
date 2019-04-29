import sys

from PyQt5.QtWidgets import *
import glob, os
from projet import Ui_MainWindow
from classes import *
from copy import deepcopy

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.commande = Commande(None, None, None, None)
        """
        COMMANDE POUR TEST
        """
        f = Plat("Frite",1,[patate],[],"",[])
        a = Plat("Kebab",6,[viande,salade,tomate,oignon],[],"",[f])
        coca = Boisson("Coca",1,[],[],"",False,25)
        m = Menu("Kebab_Frites",[a],coca,6.5)
        self.commande = Commande([m], [f, a], [coca], None)  # Commande pour tester
        self.all_commandes = [self.commande, deepcopy(self.commande), deepcopy(self.commande)]
        self.vue = "Commande"
        super(MainWindow, self).__init__()
        self.setupUi(self)

        if(self.vue == "Commande"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QHBoxLayout(frame)

            for k in self.all_commandes:
                self.textEdit = QTextEdit(self)
                self.textEdit.setContentsMargins(0,0,0,0)
                s = ""
                if k.menus:  # Je rassemble tous les plats et les boissons pour que ce soit plus lisible
                    for i in k.menus:
                        k.plats.append(i.plats[0])
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
                obj.addWidget(self.textEdit)

            print("Bla")

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


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
