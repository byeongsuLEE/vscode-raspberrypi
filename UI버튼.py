# pyqt 설치 및 ui 사용 
##https://okjh.tistory.com/75

#어려웠던점
#loadui()로 만들었던 ui버튼을 누를떄 connect를 안해줘도 자동적으로 연결되는걸 몰라서 한번 눌렀을 때 여러번 실행되는 문제가 발생했었음  - 해결 


import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
btncheck=0
btn2check=0



class MyQtProgramming(QDialog):
    def __init__(self):
        super(MyQtProgramming, self).__init__()
        loadUi('completeUi.ui',self)
        self.setWindowTitle("Button Show")
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)       
        if(btncheck==1):
            self.pushButton_2.setEnabled(True)
            self.pushButton.setEnabled(False)
            

            

     # 버튼 클릭시 실행되는 코드 
    @pyqtSlot()
    def on_pushButton_released(self):
        self.setWindowTitle("사용자 등록창")

        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        btncheck=1       
        print('사용자 등록완료')

    
    # 문열기 버튼 누를 때 이벤트 발생
     
    def on_pushButton_2_released(self):
        self.setWindowTitle("문 열기창")
        
        
        print("문을 열었습니다")

       
    
    

app=QApplication(sys.argv)
widget=MyQtProgramming()
widget.show()
sys.exit(app.exec_())