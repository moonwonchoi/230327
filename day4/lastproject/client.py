import os
from tkinter import *
from tkinter import messagebox


#####################
#소켓관련소스
import socket, threading

HOST = '127.0.0.1'
PORT = 9999
str_text = None
str_command = None

result_cnt = 0

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
def conn():
    global client_socket
    client_socket.connect((HOST, PORT))
    top_sign.config(bg="green")
    left_txt.insert("end", "client - server connected\n")
    th = threading.Thread(target=recvmsg);
    th.start()


def disconn():
    global client_socket
    client_socket.close()
    top_sign.config(bg="red")
    left_txt.insert("end", "client - server closed\n")


def sendmsg(msg):
    global client_socket
    data = msg.encode();
    client_socket.sendall(data);
    left_txt.insert("current", msg + "\n")

def recvmsg():
    global client_socket
    print('Recv-ing');
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        msg = data.decode();
        print('Received from : ', msg);
        msgproc(msg)


def msgproc(msg):
    global str_text
    global str_command
    msg_type, msg_content = msg.split("/")

    if msg_type == "CM":
        str_command = msg_content

    else: #"AL"
        str_text =  "Recv:" + msg + "\n"
        msgbox = messagebox.showinfo( "관리자 메세지", msg_content)

def send_result(b_ok):
    global result_cnt
    result_cnt += 1
    msg = "RS/" + str(result_cnt)
    msg = msg + ":OK" if b_ok == True else msg + ":NG"
    print(msg);
    sendmsg(msg)


def send_result(b_ok):
    global result_cnt
    result_cnt += 1
    msg = "RS/" + str(result_cnt)
    msg = msg + ":OK" if b_ok == True else msg + ":NG"
    print(msg)
    sendmsg(msg)


def play_proc(b_play):
    if b_play == True:
        msg = "OP/resume"
        top_sign.config(bg="green")
    else:
        msg = "OP/stop"
        top_sign.config(bg="yellow")
    print(msg)
    sendmsg(msg)

def term():
    root.quit()
    root.destroy()


#####################
# UI    
root = Tk()
root.title("클라이언트")
root.geometry("640x380") # 가로 * 세로

top_frame = Frame(root)
left_frame = Frame(top_frame)
right_frame = Frame(top_frame)
top_frame.pack(side="top", fill="x")
left_frame.pack(side="left", fill="both")
right_frame.pack(side="left", fill="both", expand=True)
bottom_frame = Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True)

# 스크롤 바
scrollbar = Scrollbar(left_frame)
scrollbar.pack(side="right", fill="y")

# 텍스트박스
left_txt = Text(left_frame, width=50, yscrollcommand=scrollbar.set)
left_txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=left_txt.yview)

# 우측내용
top_sign = Label(right_frame, text="R(DISCONN)/Y(STOP)/G(PLAY)", \
                 width=30, height=4, borderwidth=2, relief="groove", bg="red")
top_sign.pack(side = "top", fill="both", expand=True)

btn_title = Label(right_frame, text="[10초마다 선택가능]", anchor="w")
btn_title.pack(side = "top", fill="x")

btn_frame1 = Frame(right_frame)
btn_frame1.pack(side = "top", fill="x", expand=True)
btn_OK = Button(btn_frame1, text="OK", width=10, bg="green", command=lambda: send_result(True))
btn_OK.pack(side = "left")
btn_NG = Button(btn_frame1, text="NG", width=10, bg="red", command=lambda: send_result(False))
btn_NG.pack(side = "right")


btn_frame2 = Frame(right_frame)
btn_frame2.pack(side = "bottom", fill="x", expand=True)
btn_stop = Button(btn_frame2, text="일시정지", width=10, bg="yellow", command=lambda: play_proc(False))
btn_stop.pack(side = "left")
btn_resume = Button(btn_frame2, text="재가동", width=10, bg="yellow", command=lambda: play_proc(True))
btn_resume.pack(side = "right")
    

# 하단버튼
btn_connect = Button(bottom_frame, text="서버접속", width=10, command=conn)
btn_connect.pack(side = "left")
btn_disconnect = Button(bottom_frame, text="접속종료", width=10, command=disconn)
btn_disconnect.pack(side = "left")
btn_client_term = Button(bottom_frame, text="시스템종료", width=10, command=term)
btn_client_term.pack(side = "left")

btn_msg_call = Button(bottom_frame, text="관리자호출", width=10, bg="yellow", command= lambda: sendmsg("MG/관리자 호출"))
btn_msg_call.pack(side = "right")


def read_text():
    global str_text
    global str_command
    print("read_text()", str_text, str_command);
    root.after(1000, read_text)
    if str_text != None:
        left_txt.insert("end",str_text)
        str_text = None
    
    if str_command != None:
        if str_command == "stop":
            play_proc(False)
                
        elif str_command == "resume":
            play_proc(True)

        str_command = None
    

root.after(1000, read_text)

root.mainloop()
