# Day1 1차 실습 코드 
##print("test") #표준 라이브러리에서 제공하는 기본 함수


##import os   # 다른 모듈을 로드하실 때 사용

#os.system("pause") # 로드된 os라는 모듈안에 있는 system이라는 함수사용
                   # os라는 모듈안에 구현되어있는 메소드 / 함수
#os.system("calc")

##test_var = 11    #1
##
##if test_var == 10: #2
##    test_var = 15
##else:  #3
##    print("else") #4
##
##print(test_var) #5


#"red" 이값을 가지고 있는 리터럴 (객체)를 생성
#"green", "blue" 객체를 생성합니다.
#[] 위에 값들을 가지고 있을 수 있는 컨테이너형 객체 생성 ->
                   # 그 객체 안에 값 3개 화살표 저장
#컨테이너형 객체를 지칭하는 주소값을 colors라는 식별자 (변수)에 저장합니다.
                

##colors = ["red", "green", "blue"]
##
##for c in colors:
##    print(c)
##
##print("finish")


###동적타이핑
##a = 1 #이때는 변수 a가 숫자1 리터럴을 쳐다봅니다.
##a = "str" #이때는 변수 a가 문자열 "str"을 쳐다봅니다.
##
###덕 타이핑
###클래스 선언 (객체 설계도)
##class AType:
##    def fly(self): #함수 fly (메소드)
##        print("A Type flying")  #로직 기능 코드 구현
##
###클래스 선언 (객체 설계도)
##class BType:
##    def fly(self): #함수 fly (메소드)
##        print("B Type flying")  #로직 기능 코드 구현
##
###함수를 직접 정의 구현
##def callFly(entity):
##    entity.fly()  #덕타이핑
##
###클래스 설계도 1개 -> 10개의 인스턴스 entity(var_A)  fly(self)
##var_A = AType()   #클래스명 () -> 코드를 작성 -> 인스턴스화 (메모리에 올라간 그 객체)
##var_B = BType()
##
##callFly(var_A)
##callFly(var_B)


###기계어로 가기위한 코드
##def machineCodeView():
##    a = 0
##    for i in [1,2,3,4]:
##        a = a + i  #연산자 우선순위
##
##    a = a + 10
##    print(a)
##    return 10
##
##import dis
##dis.dis(machineCodeView)

#리스트 클래스의 코드를 가지고 리스트 인스턴스 생성 -> 객체 (함수, 변수[속성])
##fruits = []    #[] 리스트라는 객체를 생성해라 문법 -> fruits 식별자 (변수) 대입
##fruits.append("바나나")   #객체 (클래스 / 인스턴스 의미)
##fruits.insert(0, "키위")
##fruits[1:1] = ["사과"]   # a,b = 5,3 /// a,b = b,a   -> 3, 5   ->a 5, b 3
##print(fruits)

##data = [
##    ['a','b','c','e','f'],
##    ['f','g','h','i','j'],
##    ['k','l','m','n','o'],
##    ['p','q','r','s','t']
##]
##
##print(data[0])
##print(data[0][1])
##
##data[0][1] = 'z'
##print(data[0][1])



##for i in range(1,5,1):   #값을 생성하는 클래스(객체) -> 제네레이터 yeild
##    print(i)

##
##for n in range(2,10):
##    print("1")
##    if n!= 2 and n % 2 == 0:
##        continue
##
##    print("2")
##    for x in range(3,n):
##        print("3")
##        if n % x == 0:
##            break
##    else:
##        print('{}는 소수임'.format(n))
##
##    
##    print("4")
##
##
##def add(x,y):
##    return x+y
##
##add(10)
##
##add(11,21)
##
##
##
##
##
##int c = 10;
##c식별자 쓸거고 int 크기만큼 메모리를 할당해둘거다.
##= 10;
##
##a = 10
##a 식별자를 쓸거고, 식별자에는 주소값을 저장할 것입니다.
##10보고 만든 그 객체의 주소값이 저장될 것입니다.

#print(type([1,2,3,4]))
##
##1 #정수형 int class
##a = 1
##
##1.2345 #실수형 float class
##a = 1.2345
##
##"12345" #문자열 객체 (char -> str)
##a = "12345"
##
##[1,2,3,4] # 리스트 객체
##a = [1,2,3,4]
##
##(1,2,3,4) # 튜플 리스트 동일 (수정 X)
##a = (1,2,3,4)
##
##{1,1,2,2,3,3,4,5} # {1,2,3,4,5} SET 중복을 허용하지 않는 객체
##a = {1,1,2,2,3,3,4,5}
##
##{"1234":10000, "cafe" : 123000}  #dict key:value
##a = {"1234":10000, "cafe" : 123000}
##
##
##

##import sys
##
##num_one = 3000
##num_two = num_one
##num_thr = num_one
##num_four = num_one
##
##print(type(num_two))
##
##print(sys.getrefcount(num_two))
##
##num_one = 3001
##print(sys.getrefcount(num_one))
##
##a = 10
##a = b


a = 10 #10객체 생성 a에 대입 (= 대입연산자)
b = 11 # 11객체 생성 b에 대입
a = b  # b참조를 a에 대입

a = a + 10   # 10이라는 새로운 객체 만들고, a에 가 쳐다보는 10값과 더합니다
           # 더한 결과로 새로운 객체를 만들어서 a에 대입합니다.

a = str(a)

print(type(a))  #class 'str'


majorver = 0
minorver = 0

def mod_minor_done():
    global minorver
    minorver = minorver + 1
    
def mod_major_done():
    global majorver
    majorver = majorver + 1

# 0000.0000 -> 1.0

mod_minor_done(); mod_minor_done(); mod_major_done()

# v1.2

versiontext = "v" + str(majorver) + "." + str(minorver)
print(versiontext)

print('v{}.{}'.format(majorver, minorver))

print("v", end = "")
print(majorver, end = "")
print(".", end = "")
print(minorver)







































































































