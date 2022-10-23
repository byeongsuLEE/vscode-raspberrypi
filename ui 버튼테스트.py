# pyqt 설치 및 ui 사용 
##https://okjh.tistory.com/75
#다른 py 파일 실행 시키기 
#https://www.delftstack.com/ko/howto/python/python-run-another-python-script/

#어려웠던점S
#exec()함수로 다른 py 파일을 실행할때 경로문제가 발생해서 exec를 사용하지 못하고 코드를 그대로 씀. -sub process 함수를 사용하여 해결 
#loadui()로 만들었던 ui버튼을 누를떄 connect를 안해줘도 자동적으로 연결되는걸 몰라서 한번 눌렀을 때 여러번 실행되는 문제가 발생했었음  - 해결 

#다음 해야할거
# 터치스크린으로 cam 끄게 하기 , 몇초뒤에 자동으로 꺼지는식으로?
#  침입 기록을 어떻게 자동화 할것인가?
# 지라 바꾸기 


#자동적으로 이미지 저장 된 거  삭제
# 


# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import cv2
import sys
import numpy as np
import os
import pigpio #pigpio library
from time import sleep #pigpio library
class MyQtProgramming(QDialog):
    def __init__(self):
        super(MyQtProgramming, self).__init__()
        loadUi('practiceui.ui',self)
        self.setWindowTitle("Button Show")
        
        
    
    # 버튼 클릭시 실행되는 코드 
    @pyqtSlot()
    def on_pushButton_released(self):
        self.setWindowTitle("사용자 등록창")
        subprocess.call("python 모터랑얼굴인식.py", shell=True)
        
#문열기


            # 문열기 버튼 누를 때 이벤트 발생 
    def on_pushButton_2_released(self):
        self.setWindowTitle("문 열기창")
#문열기


            
          
        pi = pigpio.pi() 
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainers/trainer.yml')
        cascadePath = "haarcascade/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath);
        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter
        id = 0
        openscore =0
        # names related to ids: example ==> loze: id=1,  etc

        names = ['parkgiwon', 'parkgiwon', 'None','chs', 'ksw']

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:
            ret, img =cam.read()
            #img = cv2.flip(img, -1) # Flip vertically
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )

            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                # Check if confidence is less them 100 ==> "0" is perfect match
                if (confidence < 100):
                    id = names[id]
                    openscore = round(100 - confidence)
                    confidence = "  {0}%".format(round(100 - confidence))
                    
                    
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
            cv2.imshow('camera',img) 
            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if openscore >55:
                #문 여는 파일
                
                
                pi.set_servo_pulsewidth(18, 0)
                sleep(0.5)        
                #time.sleep(0.5)
                pi.set_servo_pulsewidth(18, 500)
                sleep(0.5)

                pi.set_servo_pulsewidth(18, 1500)
                sleep(0.5)
                print("문이 열렸습니다")

                #time.sleep(0.5)
                check =False
                out = True
                break
            
            if k == 27:
                break
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()




        
        #subprocess.call("python 모터랑 얼굴인식.py", shell=True)
        
        print("문을 열었습니다")
            
        def on_pushButton_3_released(self):
            self.setWindowTitle("침입기록창")
           
    
    

app=QApplication(sys.argv)
widget=MyQtProgramming()
widget.show()
sys.exit(app.exec_())


