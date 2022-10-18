# pyqt 설치 및 ui 사용 
##https://okjh.tistory.com/75
import cv2
import os
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import numpy as np
from PIL import Image



class MyQtProgramming(QDialog):
    def __init__(self):
        super(MyQtProgramming, self).__init__()
        loadUi('practiceui.ui',self)
        self.setWindowTitle("Button Show")
        
    # 버튼 클릭시 실행되는 코드 
    @pyqtSlot()
    def on_pushButton_released(self):
        self.setWindowTitle("사용자 등록창")
        # 학습전 이미지 저장 단계 


        # 학습전 이미지 저장 단계 


        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video width
        cam.set(4, 480) # set video height
        face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

        # For each person, enter one numeric face id
        #face_id = input('\n enter user id end press <return> ==>  ')
        face_id=1
        print("\n [INFO] Initializing face capture. Look the camera and wait ...")

        # Initialize individual sampling face count
        count = 0
        while(True):
            ret, img = cam.read()
            #img = cv2.flip(img, -1) # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                count += 1
                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 100: # Take 30 face sample and stop video
                break
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()

# 저장된 이미지를 이용해 학습하기


        # 저장된 이미지를 이용해 학습하기

        # Path for face image database
        #path = 'dataset'
        path = 'dataset'

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        detector = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml");

        # function to get the images and label data
        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
            faceSamples=[]
            ids = []
            for imagePath in imagePaths:
                PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
                img_numpy = np.array(PIL_img,'uint8')

                id = int(os.path.split(imagePath)[-1].split(".")[1])
                faces = detector.detectMultiScale(img_numpy)
                for (x,y,w,h) in faces:
                    faceSamples.append(img_numpy[y:y+h,x:x+w])
                    ids.append(id)
            return faceSamples,ids
        print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        faces,ids = getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        recognizer.write('trainers/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
        # Print the numer of faces trained and end program
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

                
    def on_pushButton_2_released(self):
        self.setWindowTitle("문 열기창")
        #카메라 인식하기 


        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainers/trainer.yml')
        cascadePath = "haarcascade/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath);
        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter
        id = 0
        openscore =0
        # names related to ids: example ==> loze: id=1,  etc
        # 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.
        names = ['parkgiwon', 'byeongsu', 'None','chs', 'ksw']

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
            if openscore >65:
                print("사용자 인식완료 ")
                break
            if k == 27:
                break
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()





    def on_pushButton_3_released(self):
        self.setWindowTitle("침입기록")  

app=QApplication(sys.argv)
widget=MyQtProgramming()
widget.show()
sys.exit(app.exec_())