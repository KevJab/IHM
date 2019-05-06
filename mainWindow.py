from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from classes import *
from copy import deepcopy
import sys
import glob, os

class MyMainWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)

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
        self.commande = Commande([m], [poulet, crevette], [pepsi], None)  # Commande pour tester
        self.all_commandes = [self.commande, deepcopy(self.commande), deepcopy(self.commande)]
        self.vue = "Plats"

        self.resize(800, 500)
        self.setWindowTitle("RestApp")

        #######################################################

        # Creating the top bar
        self.top_bar = QToolBar("top")
        self.top_bar.setMovable(False)
        self.top_bar.setIconSize(QSize(45,45))

        # Adding the corresponding buttons
        self.home_action = QAction(QIcon("Icons/home.svg"), "Home")
        self.home_action.triggered.connect(self.home)
        self.top_bar.addAction(self.home_action)

        self.menus_action = QAction(QIcon("Icons/assiette_couverts.png"), "Menus")
        self.menus_action.triggered.connect(self.menus)
        self.top_bar.addAction(self.menus_action)

        self.payment_action = QAction(QIcon("Icons/paiement.png"), "Pay")
        self.payment_action.triggered.connect(self.payment)
        self.top_bar.addAction(self.payment_action)

        self.orders_action = QAction(QIcon("Icons/resto.png"), "Orders")
        self.orders_action.triggered.connect(self.orders)
        self.top_bar.addAction(self.orders_action)

        # Creating the toolbar itself
        self.addToolBar(self.top_bar)

        #######################################################

        # Creating the main widget, a Stack
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Adding all views to the stack
        self.home_widget = QTextEdit()
        self.home_widget.setText("Home")
        self.stack.addWidget(self.home_widget)

        # A list of menus. There are 4 tabs: Menus, drinks, meals and daily offers
        self.menu_widget = QTabWidget()
        self.menu_widget.setMovable(False)
        self.menu_widget.setTabPosition(QTabWidget.West)
        self.menu_widget.currentChanged.connect(self.change_tab)
        self.menu_widget.setIconSize(QSize(82, 82))
        ###
        self.menus_widget = QWidget()
        self.menu_widget.addTab(self.menus_widget, QIcon("Icons/menus.jpg"), "")
        self.menu_layout = QVBoxLayout(self.menus_widget)
        ###
        self.boissons_widget = QWidget()
        self.menu_widget.addTab(self.boissons_widget, QIcon("Icons/verre.jpg"), "")
        self.boisson_layout = QVBoxLayout(self.boissons_widget)
        ###
        self.plats_widget = QWidget()
        self.menu_widget.addTab(self.plats_widget, QIcon("Icons/assiette_couverts.png"), "")
        self.plats_layout = QVBoxLayout(self.plats_widget)
        ###
        self.platsDuJour_widget = QWidget()
        self.menu_widget.addTab(self.platsDuJour_widget, QIcon("Icons/date.png"), "")
        self.plats_du_jour_layout = QVBoxLayout(self.platsDuJour_widget)
        ###
        self.stack.addWidget(self.menu_widget)

        # A list of all current orders
        self.orders_widget = QWidget()
        self.layout_order = QHBoxLayout(self.orders_widget)
        self.stack.addWidget(self.orders_widget)

        # A recap of all you consumed
        self.payment_widget = QWidget()
        self.payment_layout = QVBoxLayout(self.payment_widget)
        #TODO ajouter option de paiements séparés?
        self.stack.addWidget(self.payment_widget)

        self.edit_menu_widget = QWidget()
        #TODO ??? still left to do
        self.stack.addWidget(self.edit_menu_widget)

        self.edit_home_widget = QWidget()
        #TODO ??? still left to do (Eve)
        self.stack.addWidget(self.edit_home_widget)

    ###############################################

    def home(self): #TODO signal quand on appuie sur le bouton home
        self.stack.setCurrentWidget(self.home_widget)

    ###############################################

    def menus(self): 
        self.stack.setCurrentWidget(self.menu_widget)

    ###############################################

    def payment(self): 
        self.stack.setCurrentWidget(self.payment_widget)
        deleteItemsOfLayout(self.payment_layout)

        self.textEdit = QTextEdit()
        self.textEdit.setContentsMargins(0,0,0,0)
        s = ""
        total = 0
        font = "helvetica"

        s += "<b>Boissons</b>\n"
        if self.commande.boissons:
            s += "<pre><font face='"+font+"'>"
            for n in self.commande.boissons:
                s+= n.nom + "\t\t\t" + str(n.prix) + "€\n"
                total += n.prix
            s += "</font></pre> <br>\n"
        s += "<b>Plats</b>\n"
        if self.commande.plats:
            s += "<pre><font face='"+font+"'>"
            for m in self.commande.plats:
                s += m.nom + "\t\t\t" + str(m.prix) + "€\n"
                total += m.prix
            s += "</font></pre> <br>\n"
        s += "<b>Menus</b>\n"
        if self.commande.menus:
            s += "<pre><font face='"+font+"'>"
            for o in self.commande.menus:
                s += o.nom + "\t\t" + str(o.prix) + "€\n"
                total += o.prix
            s += "</font></pre>\n"

        s += "<hr><b>Total</b> \n<pre><font face='"+font+"'>\t\t\t" + str(total) + "€</font></pre>"

        self.textEdit.setHtml(s)
        self.textEdit.adjustSize()
        btn = QPushButton('Payer', self)
        btn.resize(50, 50)
        btn.setStyleSheet("background-color: yellow;")
        self.payment_layout.addWidget(self.textEdit)
        self.payment_layout.addWidget(btn)

    ###############################################

    def orders(self): 
        self.stack.setCurrentWidget(self.orders_widget)
        deleteItemsOfLayout(self.layout_order)
        for k in self.all_commandes:
            obj2 = QVBoxLayout()
            self.textEdit = QTextEdit()
            self.textEdit.setContentsMargins(0,0,0,0)
            s = ""
            font = "helvetica"
            if k.menus:  # Je rassemble tous les plats et les boissons pour que ce soit plus lisible
                for i in k.menus:
                    for j in i.plats:
                        k.plats.append(j)
                    k.boissons.append(i.boisson)
            k.menus = None
            s += "<b>Boissons</b> \n"
            if k.boissons:
                s += "<pre><font face='"+font+"'>"
                for n in k.boissons:
                    s+= n.nom + "\n"
                s += "</font></pre>"
            s += "<b>Plats</b> \n"
            if k.plats:
                s += "<pre><font face='"+font+"'>"
                for m in k.plats:
                    s += m.nom + "\n"
                s += "</font></pre>"
            self.textEdit.setHtml(s)
            self.textEdit.adjustSize()
            btn = QPushButton('Terminer', self)
            btn.resize(50, 50)
            btn.setStyleSheet("background-color: red;")
            obj2.addWidget(self.textEdit)
            obj2.addWidget(btn)
            self.layout_order.addLayout(obj2)
    ###############################################

    def change_tab(self, tab_num): 
        # tab_num = 1 (menus), 2 (boissons), 3 (plats) ou 4 (plats du jour)
        if tab_num == 1:
            deleteItemsOfLayout(self.menu_layout)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Menu_*.txt')):
                f = open(txt_file, "r")
                txt = f.readlines()
                t = QTextEdit(self)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                t.setPlainText(''.join(map(str, txt)))
                self.menu_layout.addWidget(t)
                self.menu_layout.addWidget(btn)
        elif tab_num == 2:
            deleteItemsOfLayout(self.boisson_layout)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Boisson_*.txt')):
                f = open(txt_file, "r")
                txt = f.readlines()
                t = QTextEdit(self)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                t.setPlainText(''.join(map(str, txt)))
                self.boisson_layout.addWidget(t)
                self.boisson_layout.addWidget(btn)
        elif tab_num == 3:
            deleteItemsOfLayout(self.plats_layout)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Plat_*.txt')):
                f = open(txt_file, "r")
                txt = f.readlines()
                t = QTextEdit(self)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                t.setPlainText(''.join(map(str, txt)))
                self.plats_layout.addWidget(t)
                self.plats_layout.addWidget(btn)

        elif tab_num == 4:
            deleteItemsOfLayout(self.plats_du_jour_layout)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Plat_*.txt')):
                f = open(txt_file, "r")
                txt = f.readlines()
                t = QTextEdit(self)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                t.setPlainText(''.join(map(str, txt)))
                self.plats_du_jour_layout.addWidget(t)
                self.plats_du_jour_layout.addWidget(btn)


def deleteItemsOfLayout(layout):
     if layout is not None:
         while layout.count():
             item = layout.takeAt(0)
             widget = item.widget()
             if widget is not None:
                 widget.setParent(None)
             else:
                 deleteItemsOfLayout(item.layout())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()



    window.show()
    app.exec()
