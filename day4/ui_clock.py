import tkinter               #tkinter lib import
import tkinter.font          #tkinter font 설정       

import time                  #날짜 시간 등을 가져오기 위해서
from threading import Thread #Thread 생성하기 위해서 쓰레드 모듈

timerid = None               #viewtime에서 설정한 timer의 id를 기록하기 위해서
                             #btnStop에서 해당 timer를 취소 시키기 위함
thid = None                  #생성한 Thread ID를 저장함
                             #-> btnStop 쓰레드가 종료되지 않음 기다리기 위해
                             #-> btnExit 때 쓰레드 종료를 체크하기 위함
                             #-> 프로그램 종료 전 쓰레드 종료를 체크하기 위함
  
g_exit_th = False            #Thread 루프에서 g_exit_th 변수값이 true면 이제
                             # 루프를 빠져나가라 를 위함

def btnStart(): # 콜백함수, 핸들러
    global timerid
    global thid
    global g_exit_th
    print("OK 버튼이 클릭되었습니다.")
    
    viewTime(" start")
    g_exit_th = False
    thid = Thread(target=loopTHMsg, args=(lbTHMsg,))
    thid.start()

def viewTime(msg):
    global timerid
    global thid
    global g_exit_th
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    lbTime.config(text = str(now) + msg)
    timerid=window.after(1000, viewTime, " after")
    

def btnStop(): # 콜백함수, 핸들러
    global timerid
    global thid
    global g_exit_th
    print("Cancel 버튼이 클릭되었습니다.", timerid)
    window.after_cancel(timerid)
    g_exit_th = True
    thid.join()

def btnExit(): # 콜백함수, 핸들러
    global timerid
    global thid
    global g_exit_th
    print("Exit 버튼이 클릭되었습니다.")
    g_exit_th = True
    thid.join()
    window.destroy()

def loopTHMsg(obj):
    msgcounter = 0
    while g_exit_th == False:
        msgcounter = 1 if msgcounter >= 3 else msgcounter + 1       
        msgtext = "" 
        for x in range(msgcounter):
            msgtext = msgtext + "."
        print(msgtext)
        obj.config(text = msgtext)
        time.sleep(0.5)

    print("쓰레드 종료")

window = tkinter.Tk()

window.title("UI")
window.geometry("640x100+200+100")

myfont=tkinter.font.Font(family="맑은 고딕", size=13, weight="bold")

lbTime = tkinter.Label(window, width=100, bg = "yellow")
lbTime.pack()
lbTHMsg = tkinter.Label(window, width=100, bg = "green", font = myfont)
lbTHMsg.pack()
lbBtnArea = tkinter.Label(window, width=50, height=5)
lbBtnArea.pack()

btStart = tkinter.Button(lbBtnArea, width=20, text = "START", fg = "red", command = btnStart)
btStop = tkinter.Button(lbBtnArea, text = "STOP", bg = "yellow", command = btnStop)
btExit = tkinter.Button(lbBtnArea, text = "EXIT", bg = "yellow", command = btnExit)

btStart.pack(side="left", padx = 10, pady = 10)
btStop.pack(side="left", padx = 10, pady = 10)
btExit.pack(side="left", padx = 10, pady = 10)

window.mainloop()
print("closed window")
g_exit_th = True
thid.join()
print("closed thread")

#------
