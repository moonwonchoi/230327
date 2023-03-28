# iterator 구현해보기
# MyCollection은 iterable하면서 iterator임 
# iterator를  __iter__와 __next__를 구현해야함
class MyCollection:   # class Mycollection이름의 클래스를 정의
    def __init__(self): # 객체가 생성이 될때 자동으로 호출되는 함수
        self.size = 3 # 이 클래스 멤버변수 size, data
        self.data = [0,1,2] #range(0, self.size) 

    def __iter__(self):
        #str_iterator 생성해서 return
        self.index = 0 # iterator 활용할때 어디까지 추출했는지 저장하는 변수
        return self

    def __next__(self): # next()
        if self.index >= self.size: #index > total size
            raise StopIteration # 예외를 발생(이벤트를 발생)

        n = self.data[self.index] #data에 접근해서 값을 가지고 온 후 리턴
        self.index += 1 #index + 1
        return n

c_tor = iter(MyCollection())
print(next(c_tor)) #0
print(next(c_tor)) 
print(next(c_tor)) #raise stopiteration
