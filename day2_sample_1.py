#230328 sample code

# 일반적인 예시
a = 10
b= 20

c = b
b = a
a = c

#python
a = 10
b = 20
# swap
a,b = b,a
print(a, ",", b)
# unpacking
a,b,c = (15,25,35)
print(a, ",", b, ",", c)
# packing
x = 15, 25, 35
print(x)


#내포 (어떤 컨테이터형 객체 안에 값들을 생성하여 내포하는 문법)
#[표현식 for 변수 in 반복가능한 객체]
listcomp=[x * 2 for x in [1,2,3]]
print(listcomp)

listcomp = []
for x in [1,2,3]:
    listcomp.append(x * 2)

print(listcomp)

#[표현식 for 변수 in 반복가능한 객체 if 조건문]
#1~10
#짝수만
#[2,4,6,8,10]

listcomp2 = []
for x in range(1, 10+1):  # 1
    if x % 2 == 0:          # 1 # 2
        listcomp2.append(x) # 1 # 2
print(listcomp2)

listcomp3 = [x for x in range(1, 10+1) if x % 2 == 0]
print(listcomp3)

# [표현식 for 변수 in 반복가능한 객체 for 이중포문]
# 1 ~ 3, 10~15 
# [10,11,12,13,14,15,20,22,26,28~~~]

listcomp4 = []
for x in range(1,3+1):
    for y in range(10,15+1):
        listcomp4.append(x*y)

print(listcomp4)

listcomp5 = [x*y for x in range(1,3+1) for y in range(10,15+1)]
print(listcomp5)

a = 1
b = 2
versiontext = f"v{a}.{b}"
print(versiontext)


class testslot:    #class 생성 키워드
    __slots__ = ('x','y','z')
    def __init__(self, x, y, z):  #초기화 관련 함수를 선언(재정의)
       self.x = x
       self.y = y
       self.z = z

    def __str__(self): #재정의
       return f"x = {self.x}, y = {self.y}, z = {self.z}"

p1 = testslot(1,2,3)  #인스턴스 생성(1,2,3)
p2 = testslot(4,5,6)
print(p1)  # __str__
print(p2)

p1.new_var = 10































































