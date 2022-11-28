def uistart() :
    import sys
    from PyQt5.QtCore import pyqtSlot
    from PyQt5.QtWidgets import QApplication, QDialog
    from PyQt5.uic import loadUi
    import 사진찍고학습 as pt
    import 모터로문열기완성본 as openlocker
    import os
    btncheck=0
    btn2check=0
    registercomplete =False;
    registercomplete=os.path.isfile("dataset/User.1.100.jpg")
    

    class MyQtProgramming(QDialog):
        def __init__(self):
            super(MyQtProgramming, self).__init__()
            loadUi('completeUi.ui',self)
            self.setWindowTitle("Button Show")
            if(registercomplete==True):
                self.pushButton.setEnabled(False)
                self.pushButton_2.setEnabled(True)
            else :
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(False)
                
                   
            if(btncheck==1):
                self.pushButton_2.setEnabled(True)
                self.pushButton.setEnabled(False)
                

        @pyqtSlot()
        def on_pushButton_released(self):
            self.setWindowTitle("사용자 등록창")
            pt.picturetrain()
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            btncheck=1 
            
        def on_pushButton_2_released(self):
            self.setWindowTitle("문 열기창")
            openlocker.open()
             

    app=QApplication(sys.argv)
    widget=MyQtProgramming()
    widget.show()
    sys.exit(app.exec_())
    
