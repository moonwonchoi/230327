def ShowMenu():   
     pass
def BuyItem(num):    
    pass 
def ShowSellList():
    pass
    
def CheckPassword():
    pass
 
menu = ("콜라", "사이다", "생수", "커피")
price = (1200, 1000, 700, 1500)
money = 0
money = int( input("돈을 투입하세요 : ") )
selllist = {}

while True:
    pass


"""
돈을 투입하세요 : 10000
[자판기 판매 메뉴]
# 1 . 콜라 	가격 :  1200
# 2 . 사이다 	가격 :  1000
# 3 . 생수 	가격 :  700
# 4 . 커피 	가격 :  1500

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