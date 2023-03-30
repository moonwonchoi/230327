import traceback

a = []
try:
    raise Exception("원인1", "원인2") # 수동 예외 발생 코드
    a[0] = 0  #NameError 발생
except KeyError as keyError:
    pass
    
except Exception as e:  #예외 최상위 클래스 타입으로 분기 처리
    print(e)
    print(type(e)) #예외가 무슨 타입인지?
    print(type(e) == NameError and "NAMEERROR")
    print(type(e).__name__.upper() == "nameerror") #"NameError"
    print(e.args)

    print(traceback.format_exc())
except:
    print("error가 발생했습니다")

print("프로그램 종료")

