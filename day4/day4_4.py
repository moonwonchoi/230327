class Sample:
    sharename = "basic"

    def __init__(self, value):
        self.v_ins = value
        self.__name = "나의 이름입니다" + str(value)

    @classmethod
    def changeShareName(cls, new_name):
        print(cls.sharename)
        cls.sharename = new_name
        print(cls.sharename)

    @property 
    def name(self): ##getter
        #권한체크
        #return 
        return self.__name
    
    @name.setter
    def name(self, name): ##setter
        #유효성
        # true
        self.__name = name



ins1 = Sample(1)
ins2 = Sample(2)

ins1.changeShareName("new-name")
ins2.changeShareName("new-name2")
Sample.changeShareName("new-name3")
