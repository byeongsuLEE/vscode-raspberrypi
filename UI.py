# pyqt 설치 및 ui 사용 
##https://okjh.tistory.com/75
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MyQtProgramming(QDialog):
    def __init__(self):
        super(MyQtProgramming, self).__init__()
        loadUi('practiceui.ui',self)
        self.setWindowTitle("Button Show")
        
    # 버튼 클릭시 실행되는 코드 
    @pyqtSlot()
    def on_pushButton_released(self):
        self.setWindowTitle("사용자 등록창")
        
    def on_pushButton_2_released(self):
        self.setWindowTitle("문 열기창")
        
    def on_pushButton_3_released(self):
        self.setWindowTitle("침입기록")  
                      
app=QApplication(sys.argv)
widget=MyQtProgramming()
widget.show()
sys.exit(app.exec_())