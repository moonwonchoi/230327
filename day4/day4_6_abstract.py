from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print("나 공부함")
    def go_to_school(self):
        print("나 학교감")

james = Student()
james.study()
james.go_to_school()
