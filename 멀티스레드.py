from multiprocessing import Process
import time
import subprocess
import 침입센서작동시사진저장 as dsps
import UI as ui
def func0():
    dsps.start()

    
def func1():
    ui.uistart()
    


if __name__ == '__main__':
    p0 = Process(target=func0)
    p1 = Process(target=func1)
    p0.start()
    p1.start()
    p0.join()
    p1.join()
    print("main process is done")


