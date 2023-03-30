class Student:
    # 변수
    name = "Jessy"
    korean = 20
    english = 30
    namth = 40

    # 함수
    def do_midterm_exam(self): #인스턴스 함수
        print("do_midterm_exam")


a = Student()  #student 클래스 설계도를 가지고 인스턴스를 생성합니다. => a
a.do_midterm_exam() # a 인스턴스 -> 해당 인스턴스를 이용해서 클래스에서 정의한
                    # do_midterm_exam(self) 함수를 호출합니다.
                    # self -> 인스턴스용 함수를 말합니다.
b = Student()
b.do_midterm_exam()
        
Student.do_midterm_exam()
