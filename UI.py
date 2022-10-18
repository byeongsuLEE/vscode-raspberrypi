import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MyQtProgramming(QDialog):
    def __init__(self):
        super(MyQtProgramming, self).__init__()
        loadUi('a.ui',self)
        self.setWindowTitle("My Hello Program")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label.setText('Welcome : '+self.lineEdit.text())
        
app=QApplication(sys.argv)
widget=MyQtProgramming()
widget.show()
sys.exit(app.exec_())