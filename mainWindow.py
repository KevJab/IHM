from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MyMainWindow(QMainWindow):

	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
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
		###
		self.boissons_widget = QWidget()
		self.menu_widget.addTab(self.boissons_widget, QIcon("Icons/verre.jpg"), "")
		###
		self.plats_widget = QWidget()
		self.menu_widget.addTab(self.plats_widget, QIcon("Icons/assiette_couverts.png"), "")
		###
		self.platsDuJour_widget = QWidget()
		self.menu_widget.addTab(self.platsDuJour_widget, QIcon("Icons/date.png"), "")
		###
		self.stack.addWidget(self.menu_widget)
		
		# A list of all current orders
		self.orders_widget = QWidget()
		#FIXME remplir ce widget lors de son chargement (méthode orders)
		self.stack.addWidget(self.orders_widget)
		
		# A recap of all you consumed
		self.payment_widget = QWidget()
		#FIXME idem (méthode payment)
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
	
	def menus(self): #FIXME signal quand on appuie sur le bouton menus
		self.stack.setCurrentWidget(self.menu_widget)
	
	###############################################
	
	def payment(self): #FIXME signal quand on appuie sur le bouton "payer"
		self.stack.setCurrentWidget(self.payment_widget)
	
	###############################################
	
	def orders(self): #FIXME signal pour quand on appuie sur le bouton "commandes"
		self.stack.setCurrentWidget(self.orders_widget)
		
	###############################################
	
	def change_tab(self, tab_num): #FIXME signal pour le changement de focus dans l'onglet Menus
		# tab_num = 1 (menus), 2 (boissons), 3 (plats) ou 4 (plats du jour)
		pass


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyMainWindow()
	
	
	
	window.show()
	app.exec()
