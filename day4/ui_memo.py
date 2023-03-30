import os
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("메모장")
root.geometry("640x480") # 가로 * 세로

# 열기, 저장 파일 이름
filename = "저장됐을 때 파일 이름"

def open_file():
    filename = askopenfilename(title = "파일 선택", filetypes = (("텍스트 파일", "*.txt"),("모든 파일", "*.*")))
    f = open(filename,"r", encoding="utf-8")
    tempFileData = f.read()
    f.close()
    txt.delete(1.0, END)
    txt.insert(1.0, tempFileData)

def save_file():
    filename = asksaveasfilename(title = "파일 선택", filetypes = (("텍스트 파일", "*.txt"),("모든 파일", "*.*")))
    print(filename)
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

def clear():
    txt.delete(1.0, END)

def term():
    root.quit()
    root.destroy()



content_frame = Frame(root)
content_frame.pack(side="top", fill="both", expand=True)
bottom_frame = Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True)

# 스크롤 바
scrollbar = Scrollbar(content_frame)
scrollbar.pack(side="right", fill="y")

def counter(obj):
    #get(start, end=None)
    txt_text = txt.get(1.0, "end-1c")  # end 위치에서 빼기 1char   
    cnt = str(len(txt_text))    
    S_Var1.set(cnt + "자")

# 본문 영역
txt = Text(content_frame, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
txt.bind('<KeyRelease>', counter)
scrollbar.config(command=txt.yview)

# 하단 영역
S_Var1 = StringVar()
S_Var1.set("empty")
label = Label(bottom_frame, textvariable = S_Var1, width=10) #width 글자 단위
label.pack(side = "left")
btn_load = Button(bottom_frame, text="load", width=10, command=open_file)
btn_load.pack(side = "left")
btn_save = Button(bottom_frame, text="save", width=10, command=save_file)
btn_save.pack(side = "left")
btn_clear = Button(bottom_frame, text="clear", width=10, command=clear)
btn_clear.pack(side = "left")
btn_exit = Button(bottom_frame, text="exit", width=10, command=term)
btn_exit.pack(side = "left")


root.mainloop()
