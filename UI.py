import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MyQtProgramming(QDialog):
    def __init__(self):
        super(MyQtProgramming, self).__init__()
        loadUi('practiceui.ui',self)
        self.setWindowTitle("Button Show")
        
        
app=QApplication(sys.argv)
widget=MyQtProgramming()
widget.show()
sys.exit(app.exec_())