from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MyMainWindow(QMainWindow):

	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
		self.resize(800, 500)
		self.setWindowTitle("RestApp")
				
		# Creating the top bar
		self.top_bar = QToolBar("top")
		self.top_bar.setMovable(False)
		
		# Adding the corresponding buttons
		self.home_action = QAction(QIcon("Icons/resto.png"), "Home")
		self.home_action.triggered.connect(self.sayHi)
		self.top_bar.addAction(self.home_action)	
		#TODO add more
		
		self.addToolBar(self.top_bar)
		
		# Creating the main widget, a Stack
		self.stack = QStackedWidget(self)
		self.setCentralWidget(self.stack)
		
		# Adding all views to the stack	
		self.home_widget = QTextEdit()
		self.home_widget.setText("Home")
		self.stack.addWidget(self.home_widget)
		
		self.menu_widget = QTabWidget()
		#TODO
		self.stack.addWidget(self.menu_widget)
		
		self.orders_widget = QWidget()
		#TODO
		self.stack.addWidget(self.orders_widget)
		
		self.payment_widget = QWidget()
		#TODO
		self.stack.addWidget(self.payment_widget)
		
		self.edit_menu_widget = QWidget()
		#TODO
		self.stack.addWidget(self.edit_menu_widget)
		
		self.edit_home_widget = QWidget()
		#TODO
		self.stack.addWidget(self.edit_home_widget)
		

	def sayHi(self):
		self.home_widget.setText("Welcome back home!")
		self.stack.setCurrentWidget(self.home_widget)




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyMainWindow()
	
	
	
	window.show()
	app.exec()
