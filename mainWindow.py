from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from classes import *
from copy import deepcopy
import sys
import glob, os
import dessin
import modif_chaises
import dessin_modif

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
        self.home_widget = QWidget()
        self.home_layout = QHBoxLayout(self.home_widget)
        self.stack.addWidget(self.home_widget)

        # A list of menus. There are 4 tabs: Menus, drinks, meals and daily offers
        self.menu_widget = QTabWidget()
        self.menu_widget.setMovable(False)
        self.menu_widget.setTabPosition(QTabWidget.West)
        self.menu_widget.setIconSize(QSize(82, 82))
        ###
        self.menus_widget = QScrollArea()
        self.menu_widget.addTab(self.menus_widget, QIcon("Icons/menus.jpg"), "")
        self.menus_page = QWidget()
        self.menus_page.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.menus_widget.setWidget(self.menus_page)
        self.menus_layout = QVBoxLayout()
        self.menus_page.setLayout(self.menus_layout)
        self.menus_widget.setWidgetResizable(True)
        ###
        self.boissons_widget = QScrollArea()
        self.menu_widget.addTab(self.boissons_widget, QIcon("Icons/verre.jpg"), "")
        self.boissons_page = QWidget()
        self.boissons_page.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.boissons_widget.setWidget(self.boissons_page)
        self.boissons_layout = QVBoxLayout()
        self.boissons_page.setLayout(self.boissons_layout)
        self.boissons_widget.setWidgetResizable(True)
        ###
        self.plats_widget = QScrollArea()
        self.menu_widget.addTab(self.plats_widget, QIcon("Icons/assiette_couverts.png"), "")
        self.plats_page = QWidget()
        self.plats_page.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.plats_widget.setWidget(self.plats_page)
        self.plats_layout = QVBoxLayout()
        self.plats_page.setLayout(self.plats_layout)
        self.plats_widget.setWidgetResizable(True)
        ###
        self.platsDuJour_widget = QScrollArea()
        self.menu_widget.addTab(self.platsDuJour_widget, QIcon("Icons/date.png"), "")
        self.platsDuJour_page = QWidget()
        self.platsDuJour_page.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.platsDuJour_widget.setWidget(self.platsDuJour_page)
        self.platsDuJour_layout = QVBoxLayout()
        self.platsDuJour_page.setLayout(self.platsDuJour_layout)
        self.platsDuJour_widget.setWidgetResizable(True)
        ###
        self.change_tab(0)      # effectively displays the first tab
        self.menu_widget.currentChanged.connect(self.change_tab)
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
        
        self.home()

    ###############################################

    def home(self):
        self.stack.setCurrentWidget(self.home_widget)
        deleteItemsOfLayout(self.home_layout)
        self.grid = QGridLayout()
        self.modifchaises = modif_chaises.Modif()
        self.grid.addWidget(self.modifchaises,0,0)
        bouttonPlus = QPushButton("+")
        bouttonPlus.resize(100,32)
        self.grid.addWidget(bouttonPlus,0,1)
        bouttonPlus.clicked.connect(self.ajouterChaises)
        bouttonMoins = QPushButton("-")
        bouttonMoins.resize(100,32)
        self.grid.addWidget(bouttonMoins,0,2)
        bouttonMoins.clicked.connect(self.retirerChaises)
        #partie pour les tables
        self.Nomtables = QLabel("Nombre de tables:")
        self.Nomtables.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.Nomtables, 1, 0, 1, 2)
        self.formTables = QSpinBox()
        self.grid.addWidget(self.formTables, 1, 2)
        self.formTables.valueChanged.connect(self.modifTables)
        self.obj2.addLayout(self.grid)
        self.dessin = dessin_modif.Modif(self.taille_restau, self.liste_tables, self.liste_chaises, self)
        self.obj2.addWidget(self.dessin)
        self.home_layout.addLayout(self.obj2)
        
   ###############################################

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


    ###############################################

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


    ###############################################

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

    ###############################################

    def modifXY(self, x, y):
        self.X = x
        self.Y = y
        print("XY")
        print(self.X)
        print(self.Y)
        print(self.trouverTable())

    ###############################################

    def trouverTable(self):
        nb_tables = len(self.liste_tables)
        for i in range(nb_tables):
            nb_rect = len(self.liste_tables[i])
            a, b = self.liste_tables[i][0]
            c, d = self.liste_tables[i][nb_rect-1]
            if self.X >= a*10 and self.X <= (c+1)*10 and self.Y >= b*10 and self.Y <= (d+1)*10:
                return self.liste_tables[i]

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
        html_text = "<head><style>table{ float: left;} \ntable + table {float: right;}</style></head>\n<body>"
        if tab_num == 0:
            deleteItemsOfLayout(self.menus_layout)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Menu_*.txt')):
                menu_text = self.display_food(txt_file)
                t = QTextEdit(self)
                t.setReadOnly(True)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                menu_text = html_text + menu_text + "</body>"
                t.setHtml(menu_text)
                self.menus_layout.addWidget(t)
                self.menus_layout.addWidget(btn)
            for txt_file in glob.glob(os.path.join(parent_dir, 'Menu_*.txt')):
                menu_text = self.display_food(txt_file)
                t = QTextEdit(self)
                t.setReadOnly(True)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                menu_text = html_text + menu_text + "</body>"
                t.setHtml(menu_text)
                self.menus_layout.addWidget(t)
                self.menus_layout.addWidget(btn)
            for txt_file in glob.glob(os.path.join(parent_dir, 'Menu_*.txt')):
                menu_text = self.display_food(txt_file)
                t = QTextEdit(self)
                t.setReadOnly(True)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                menu_text = html_text + menu_text + "</body>"
                t.setHtml(menu_text)
                self.menus_layout.addWidget(t)
                self.menus_layout.addWidget(btn)
            for txt_file in glob.glob(os.path.join(parent_dir, 'Menu_*.txt')):
                menu_text = self.display_food(txt_file)
                t = QTextEdit(self)
                t.setReadOnly(True)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                menu_text = html_text + menu_text + "</body>"
                t.setHtml(menu_text)
                self.menus_layout.addWidget(t)
                self.menus_layout.addWidget(btn)
            
        elif tab_num == 1:
            deleteItemsOfLayout(self.boissons_layout)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Boisson_*.txt')):
                boisson_text = self.display_drink(txt_file)
                t = QTextEdit(self)
                t.setReadOnly(True)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                boisson_text = html_text + boisson_text + "</body>"
                t.setHtml(boisson_text)
                self.boissons_layout.addWidget(t)
                self.boissons_layout.addWidget(btn)
        elif tab_num == 2:
            deleteItemsOfLayout(self.plats_layout)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Plat_*.txt')):
                #plat_text = self.display_food(txt_file)
                t = QTextEdit(self)
                t.setReadOnly(True)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                #plat_text = html_text + plat_text + "</body>"
                #t.setHtml(plat_text)
                self.plats_layout.addWidget(t)
                self.plats_layout.addWidget(btn)

        elif tab_num == 3:
            deleteItemsOfLayout(self.platsDuJour_layout)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Plat_*.txt')):
                f = open(txt_file, "r")
                txt = f.readlines()
                t = QTextEdit(self)
                t.setReadOnly(True)
                btn = QPushButton('Ajouter', self)
                btn.resize(50, 50)
                btn.setStyleSheet("background-color: green;")
                html_text += "</body>"
                t.setHtml(html_text)
                self.platsDuJour_layout.addWidget(t)
                self.platsDuJour_layout.addWidget(btn)
            
    ###############################################

    def display_food(self, filename):
        f = open(filename, "r")
        info = {}
        s = "<table>"
        for line in f.readlines():
            line = line.rstrip("\n")
            k,v = line.split(" ")
            
            if k == "Nom":
                v = " ".join(v.split("_"))
            if k == "Vegan" or k == "Epice":
                if v == "True":
                    v = True
                else :
                    v = False
            if k == "Description":
                v = ", ".join(map(lambda word: " ".join(word.split("_")), v.split(",")))
            
            info[k] = v
        
        s += "<tr><td><b>"+info["Nom"]+"</b></td></tr>"
        s += "<tr><td><i>"+info["Description"]+"</i></td></tr>"
        
        if info["Allergenes"] != "aucun":
	        s += "<tr><td><small><b>Contient: "+ ", ".join(info["Allergenes"].split(",")) +"</b></small></td></tr>"
        
        s += "</table><table>"
        s += "<tr><td colspan='2'><p align='right'>" + info["Prix"] + "</p></td></tr><tr></tr><tr>"
        if info["Vegan"]:
            s += "<td><img src='./Icons/vegan.png' width='30' height='30'></td>"
        if info["Epice"]:
            s += "<td><img src='./Icons/spicy_full.png' width='30' height='30'></td>"
        
        return s + "</tr></table>"
    
    def display_drink(self, filename):
        f = open(filename, "r")
        info = {}
        s = "<table>"
        for line in f.readlines():
            line = line.rstrip("\n")
            k,v = line.split(" ")
            
            if k == "Nom":
                v = " ".join(v.split("_"))
            if k == "Alcool":
                if v == "True":
                    v = True
                else: 
                    v = False
            
            info[k] = v
        
        s += "<tr><td><b>"+info["Nom"]+"</b></td></tr>"
        
        if info["Alcool"]:
            s += "<tr><td><i>contient de l'alcool</i></td></tr>"
        
        s += "</table><table>"
        s += "<tr><td><p>" + info["Prix"] + "</p></td></tr>"
        s += "<tr><td><p>" + info["Contenance"] + "</p></td></tr>"
        
        return s + "</table>"
            
          	
        
    

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
