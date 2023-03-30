#pip3 install pyautogui
#pip3 install pillow

import pyautogui
import time
import pyperclip

searchtext = ["서울 날씨","시흥 날씨","청주 날씨","부산 날씨","강원도 날씨"]

addr_x = 1145
addr_y = 53
start_x = 992
start_y = 220
end_x = 1656
end_y = 635

for search in searchtext:
    pyautogui.moveTo(addr_x,addr_y,1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com",interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(search) 
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    savepath = search + ".png"
    pyautogui.screenshot(savepath, region=(start_x, start_y, end_x-start_x, end_y-start_y))
