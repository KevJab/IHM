import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QListWidget,QWidget,QVBoxLayout,QTextEdit,QHBoxLayout,QFrame
import glob, os
from projet import Ui_MainWindow
import classes
class MainWindow(QMainWindow, Ui_MainWindow):
    vue = "Plats"
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        if(self.vue == "Commande"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QHBoxLayout(frame)
            self.textEdit = QTextEdit( self )
            self.textEdit.setContentsMargins(0,0,0,0)
            self.textEdit.setPlainText("Bla")
            self.textEdit.adjustSize()
            self.textEdit1 = QTextEdit( self )
            self.textEdit1.setContentsMargins(0,0,0,0)
            self.textEdit1.setPlainText("Ble")
            self.textEdit1.adjustSize()
            self.textEdit2 = QTextEdit( self )
            self.textEdit2.setContentsMargins(0,0,0,0)
            self.textEdit2.setPlainText("Bli    ")
            self.textEdit2.adjustSize()
            obj.addWidget( self.textEdit )
            obj.addWidget( self.textEdit1 )
            obj.addWidget( self.textEdit2 )
            print("Bla")
        elif(self.vue == "Plats"):
            frame = self.findChild(QFrame,"frameVueCommandes")
            frame.setEnabled(True)
            obj = QVBoxLayout(frame)
            parent_dir = 'Conso'
            for txt_file in glob.glob(os.path.join(parent_dir, 'Plat_*.txt')):
                print (txt_file)
                t = QTextEdit(self)
                t.setPlainText(txt_file)
                obj.addWidget(t)



def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

