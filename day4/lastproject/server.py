import os
from tkinter import *
from tkinter import messagebox


#####################
#소켓관련소스
import socket, threading

def msgproc(msg):
    global str_text
    msg_type, msg_content = msg.split("/")

    if msg_type == "OP":
        str_text =  "Recv:" + msg_content + "\n"

    elif msg_type == "RS":
        str_text =  "Recv:" + msg_content + "\n"

    else: #"MG"
        str_text =  "Recv:" + msg + "\n"
        msg = messagebox.showinfo( "관리자 호출",msg_content)
                                

def connected(client_socket, addr):
    print('Connected by', addr)

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
             
            msg = data.decode();
            print('Received from', addr, msg)

            msgproc(msg)
            
            
    except:
        print("except : " , addr)
    finally:
        client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 9999))

svr_th = None
stop_threads = False
str_text = None
global_client_socket = None

def server_start_th():
    global stop_threads
    global server_socket
    global str_text
    global global_client_socket
    server_socket.listen()
    print("server started\n")
    
            
    try:
        while stop_threads == False:
            client_socket, addr = server_socket.accept();
            global_client_socket = client_socket
            print("server connected\n", addr)
            str_text =  "Hello Client" + str(addr) + "\n"
            th1 = threading.Thread(target=connected, args = (client_socket, addr));
            th1.start();
            
    except:
        print("server exception");
    finally:
        str_text =  "Server OFF\n"
        
def server_on():    
    global svr_th
    svr_th = threading.Thread(target=server_start_th)
    svr_th.start()
    print("server on\n")
    left_txt.insert("end", "Server ON\n")
    
def server_off():   
    global stop_threads    
    stop_threads = True
    server_socket.close()
    print("server off\n")

def term():
    root.quit()
    root.destroy()

  


#####################
# UI
root = Tk()
root.title("서버")
root.geometry("640x480") # 가로 * 세로

top_frame = Frame(root)
left_frame = Frame(top_frame)
right_frame = Frame(top_frame)
top_frame.pack(side="top", fill="x")
left_frame.pack(side="left", fill="both")
right_frame.pack(side="left", fill="x", expand=True)
bottom_frame = Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True)

# 스크롤 바
scrollbar = Scrollbar(left_frame)
scrollbar.pack(side="right", fill="y")

# 텍스트박스
left_txt = Text(left_frame, width=50, yscrollcommand=scrollbar.set)
left_txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=left_txt.yview)

right_top_txt = Text(right_frame, width=20)
right_top_txt.pack(side="top", fill="both", expand=True)
right_bottom_txt = Text(right_frame, width=20, height=5)
right_bottom_txt.pack(side="top", fill="both", expand=True)

# 하단버튼
btn_svr_start = Button(bottom_frame, text="서버시작", width=10, command=server_on)
btn_svr_start.pack(side = "left")
btn_svr_end = Button(bottom_frame, text="서버종료", width=10, command=server_off)
btn_svr_end.pack(side = "left")
btn_svr_term = Button(bottom_frame, text="시스템종료", width=10, command=term)
btn_svr_term.pack(side = "left")


def send_ui_text():
    send_msg = "AL/" + right_bottom_txt.get(1.0, "end-1c")
    right_bottom_txt.delete(1.0, "end")
    
    left_txt.insert("end", "sended:" + send_msg + "\n")
    data = send_msg.encode();
    global_client_socket.sendall(data);
    print('sended ', send_msg)


def send_ui_command_stop():
    send_msg = "CM/stop"
    data = send_msg.encode();
    global_client_socket.sendall(data);
    print('sended ', send_msg)

    
def send_ui_command_resume():
    send_msg = "CM/resume"
    data = send_msg.encode();
    global_client_socket.sendall(data);
    print('sended ', send_msg)

btn_client_stop = Button(bottom_frame, text="일시정지", width=10, bg="yellow", command=send_ui_command_stop)
btn_client_stop.pack(side = "right")
btn_client_play = Button(bottom_frame, text="동작", width=10, bg="yellow", command=send_ui_command_resume)
btn_client_play.pack(side = "right")
btn_client_send_msg = Button(bottom_frame, text="메세지전달", width=10, bg="yellow", command=send_ui_text)
btn_client_send_msg.pack(side = "right")

def read_text():
    global str_text
    #print("read_text()", str_text);
    root.after(1000, read_text)
    if str_text == None:
        return
    left_txt.insert("end",str_text)
    str_text = None

root.after(1000, read_text)
root.mainloop()
