def Print_My_Pattern(name, age):
    print("이름은 {0}이고, 나이는 {1}살".format(name, age))
    #pass

    return "정상호출"

print(Print_My_Pattern("김길동", 40))


def func1():
    pass  #return 생략가능 => None return  => return None

def func2(input1):    #input1 = {"d":1}
    return True

func1()
func2(10)
func2({"d":1})

#위치인수
def func_example1(a, b, c):
    print(a, b, c)

func_example1(100,300,200)

#기본인수
def func_example2(a, b = 0, c = 1):
    print(a, b, c)


func_example2(100)
#func_example2()
func_example2(100, 200)  # a = 100, b = 200, c = 1

#가변인수
def func_v(*args):
    print(args, args[0])

#func_v(10)
#func_v(10,20,30)
#func_v()
a = (20,30,40)
func_v(*a)


#키워드인수 + 가변인수
def func_keyword(*args,kwparam1, kwparam2):
    pass

func_keyword(1,2,3,4,5, kwparam1 = 999, kwparam2 = 888)

#def print(*args, sep = " ", end = "\n", file = sys.stdout)


#가변 키워드 인수 => 사전형
def func_v_kw(**kwargs):
    print(kwargs)

dic1 = {"key" : 100, "name" : "hong"}
func_v_kw(**dic1)
func_v_kw(key = 100, name = "hong")


ret = input("문자를 입력하세요")
print(ret)



















































