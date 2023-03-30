class Member:
    #공통적인 속성
    #- 인스터스들마다 고유
    # --> 인스턴스변수 self.
    #- 멤버가 몇명인지 (인스터스들이 공통적으로 공유하는 내용)
    # --> 클래스변수 cls.
    #이름 name 변수 
    #학급번호(반 번호) class_num 변수
    #def __new__ #실제 메모리 할당하는 시점

    member_count = 0
    
    def __init__(self, name, num): #메모리 할당을 다 하고 마지막으로 호출하는 함수
        self.name = name
        self.num = num
        Member.member_count += 1

    def get_role(self):
        return "member"

    def __str__(self):
        return f"이름은 {self.name}, 반은 {self.num}"

    @classmethod
    def getCount(cls):
        return cls.member_count

    @classmethod
    def addCount(cls):
        cls.member_count += 1        

    @staticmethod
    def getType():
        print("static method: ", Member.member_count)
        return "static"


class Student(Member):
    def get_role(self):
        return "student"

class Teacher(Member):
    def get_role(self):
        return "teacher"

print(Member.getType())
print(Member.getCount()) ## => 0

ins_student = Student("Jay", 1)
ins_student2 = Student("Jay2", 1)
ins_teacher = Teacher("Mike", 2)
ins_teacher2 = Teacher("Mike", 2)
print(Member.getCount()) ## => 4
print(ins_student.getCount())
print(ins_student2.getCount())
print(ins_teacher.getCount())
print(ins_teacher2.getCount())





##
##print("MEMBER1:", Member.getCount())
##Member.addCount()
##print("MEMBER2:", Member.getCount())
##ins_student.addCount()
##ins_teacher.addCount()
##print("MEMBER3:", Member.getCount())
##ins_student2.addCount()
##ins_teacher2.addCount()
##print("MEMBER4:", Member.getCount())










