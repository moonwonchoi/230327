###3항연산자
###value = true일 경우 표현식 if 조건 else false일 경우 표현식
##
##a = 6
###조건 a < 5
##"abc"
##"def"
##value = "abc" if a < 5 else "def"
##print(value)
##
### a < 5 ? "abc" : "def"
##
##"or 조건 중에 앞이 true이면 뒤를 실행하지 않음"
##x = "abcdefcde"
##y = "bc"
##
##print(y in x) #멤버십 

mylist = [1,2,3,4]
print(id(mylist))
mylist.append(5)          # 새로운 객체가 생성되지 않고 기존 객체에 추가됨
print(id(mylist))
mylist = mylist + [6]     # 새로운 객체가 생성됩니다.
print(id(mylist))
mylist.extend([6,7,8])
print(id(mylist))
mylist.insert(0,10)

#del mylist[0]
#mylist.remove(1)
print(mylist.pop(1))


#참조복사
a = [100,200,300]
b = a
print("--------")
print(id(a), ",", id(b))
print(id(a[0]), ",", id(b[0]))

# 얕은 복사
a = [100,200,300]
b = a[:]
print("--------")
print(id(a), ",", id(b))
print(id(a[0]), ",", id(b[0]))

a = [[100,200,300], [400, 500, 600]]
b = a[:]
print("--------")
print(id(a), ",", id(b))
print(id(a[0]), ",", id(b[0]))
print(id(a[0][0]), ",", id(b[0][0]))

#깊은복사 
import copy
b = copy.deepcopy(a)
print("--------")
print(id(a), ",", id(b))
print(id(a[0]), ",", id(b[0]))
print(id(a[0][0]), ",", id(b[0][0]))


































