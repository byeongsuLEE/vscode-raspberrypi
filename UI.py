# pyqt 설치 및 ui 사용 
##https://okjh.tistory.com/75
#다른 py 파일 실행 시키기 
#https://www.delftstack.com/ko/howto/python/python-run-another-python-script/

#어려웠던점
#exec()함수로 다른 py 파일을 실행할때 경로문제가 발생해서 exec를 사용하지 못하고 코드를 그대로 씀. -sub process 함수를 사용하여 해결 
#loadui()로 만들었던 ui버튼을 누를떄 connect를 안해줘도 자동적으로 연결되는걸 몰라서 한번 눌렀을 때 여러번 실행되는 문제가 발생했었음  - 해결 

#다음 해야할거
# 터치스크린으로 cam 끄게 하기 , 몇초뒤에 자동으로 꺼지는식으로?
#  침입 기록을 어떻게 자동화 할것인가?
# 지라 바꾸기 


#자동적으로 이미지 저장 된 거  삭제
# 

import sys
import subprocess
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
btn1check=0
btn2check=0
btn3check=0


class MyQtProgramming(QDialog):
    def __init__(self):
        super(MyQtProgramming, self).__init__()
        loadUi('practiceui.ui',self)
        self.setWindowTitle("Button Show")
        

        self.pushButton1.setEnabled(True)
        self.pushButton2.setEnabled(False)
        self.pushButton3.setEnabled(False)
        if(btn1check==1):
            self.pushButton2.setEnabled(True)
            self.pushButton1.setEnabled(False)
            

     # 버튼 클릭시 실행되는 코드 
    @pyqtSlot()
    def on_pushButton1_released(self):
        self.setWindowTitle("사용자 등록창")

        self.pushButton1.setEnabled(False)
        self.pushButton2.setEnabled(True)
        btn1check=1
        #subprocess.call("python 얼굴찍기.py", shell=True)
        #subprocess.call("python 02_face_training.py", shell=True)

    
    # 문열기 버튼 누를 때 이벤트 발생 
    def on_pushButton2_released(self):
        self.setWindowTitle("문 열기창")
        self.pushButton3.setEnabled(True)
        #subprocess.call("python 03_face_recognition.py", shell=True)
        
        print("문을 열었습니다")
        
    def on_pushButton3_released(self):
        self.setWindowTitle("침입기록창")
       
    
    

app=QApplication(sys.argv)
widget=MyQtProgramming()
widget.show()
sys.exit(app.exec_())