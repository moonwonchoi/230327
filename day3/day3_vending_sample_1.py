def ShowMenu():   
     print("[자판기 판매 메뉴]")
     for idx, (m_name, p_value) in enumerate(zip(menu, price)): #(0, ("콜라", 1200))
         print("#", idx+1, ".", m_name, "\t가격 : ", p_value)
     print()

##     for i in range(0, len(menu)):
##         print("#", i +1, ".", menu[i], "\t가격 : ", price[i])
##     print()
     
def BuyItem(num):
    global money
    global selllist
    if money < price[num-1]:
        print("잔액이 부족합니다")
    else:
        print(menu[num-1], "구입완료")
        money = money - price[num-1]

        if menu[num-1] in selllist.keys():
            selllist[menu[num-1]] = selllist[menu[num-1]] + 1
        else:
            selllist[menu[num-1]] = 1

    print("잔액: ", money) 
    print("selllist: ", selllist)

def BuyItem_return(num, selllist, remainmoney):
    balance = remainmoney
    if money < price[num-1]:
        print("잔액이 부족합니다")
    else:
        print(menu[num-1], "구입완료")
        balance = balance - price[num-1]

        if menu[num-1] in selllist.keys():
            selllist[menu[num-1]] = selllist[menu[num-1]] + 1
        else:
            selllist[menu[num-1]] = 1

    print("잔액: ", balance) 
    print("selllist: ", selllist)
    return balance
        
     
def ShowSellList():
    print("판매량: ", selllist)
    
    
def CheckPassword():
    pw = input("비밀번호를 입력하세요:")
    if pw =="1234":
        return True

    return False
 
menu = ("콜라", "사이다", "생수", "커피")
price = (1200, 1000, 700, 1500)
money = 0
money = int( input("돈을 투입하세요 : ") )
selllist = dict()

while True:
    ShowMenu()
    sel = int(input("메뉴 번호를 선택하세요 (종료 : 0) :"))
    if sel == 0:
        break
    elif len(menu) >= sel:
        #메뉴 정상 선택
        BuyItem(sel) #1~4
        #money = BuyItem_return(sel, selllist, money)
        print("메뉴정상 선택")
    elif sel == 99:
        print("관리자메뉴")
        if CheckPassword() == True:
            ShowSellList()
        
    else:
        #메뉴 비정상 선택
        print("메뉴 비정상 선택")        
    
print(f"자판기 종료, 잔액 {money} 반환")


"""
돈을 투입하세요 : 10000


메뉴 번호를 선택하세요 (종료 : 0) : 1
콜라  구입완료
잔액 :  8800
[자판기 판매 메뉴]
# 1 . 콜라 	가격 :  1200
# 2 . 사이다 	가격 :  1000
# 3 . 생수 	가격 :  700
# 4 . 커피 	가격 :  1500

메뉴 번호를 선택하세요 (종료 : 0) : 2
사이다  구입완료
잔액 :  7800
[자판기 판매 메뉴]
# 1 . 콜라 	가격 :  1200
# 2 . 사이다 	가격 :  1000
# 3 . 생수 	가격 :  700
# 4 . 커피 	가격 :  1500

메뉴 번호를 선택하세요 (종료 : 0) : 99
비밀번호를 입력하세요 : 1234
판매량 {'콜라': 1, '사이다': 1}
[자판기 판매 메뉴]
# 1 . 콜라 	가격 :  1200
# 2 . 사이다 	가격 :  1000
# 3 . 생수 	가격 :  700
# 4 . 커피 	가격 :  1500

메뉴 번호를 선택하세요 (종료 : 0) : 0
자판기 종료, 잔액 7800 반환
"""
