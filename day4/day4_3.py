class Student:
    def __new__(cls, name):  #클래스 메소드 
        print("new", id(cls))
        return object.__new__(cls)

    #인스턴스 메소드
    def __init__(self, name):     #객체가 생성되고 처음으로 자동호출되는 초기화 함수
        self.student_name = name
        print("init", id(self))

    def method1(self):
        print("method1", id(self), f"==student_name=>{self.student_name}")

student1 = Student("james")
print(id(student1))
student2 = Student("mike")
print(id(student2))
        
student1.method1()
student2.method1()

Exception.__name__

