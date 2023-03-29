#데이터타입
v_str1 = "String'string'"
v_str2 = 'String"string"'
v_bool = True #False
v_float = 1.12
v_int = 300
v_complex = 3 + 3j
v_dict1 = { "name" : "choi", "age" : 11} #key 불면객체만, value는 무엇이든 다 가능합니다
v_dict2 = { 10: "price", (1,2) : [1,2,3]}
v_list = [3,5,6] # v_list = []
v_tuple = (4,5,6) # v_tuple = (), v_tuple = (1,), v_tuple = tuple([1])
v_set = {4,5,6}

print("------데이터타입 생성 코드 끝-------")

#문자열 제어
#문자열 여러줄로 쓸경우
multiline_str = """가나다
가나다
123"""
print(multiline_str)
print(multiline_str.replace("\n", ""))
escape_str = "1\"a"
print(escape_str)
escape_str = "엔터키를 추가하고 싶음\n다음라인" # \t 탭
print(escape_str)

print("------문자열 제어1 참고 코드 끝-------")

#연산자
# + - * / -> // 몫, % 나머지, ** 제곱
v1 = 10
v2 = 3
print(v1 // v2)
print(v1 % v2)
print(v1 ** v2)

print("------자주 사용하는 연산자 참고 코드 끝-------")


# 연산자 -> 매직메서드
class opSample:
    def __radd__(self, a):
        print("radd", a)
        return self
    def __iadd__(self, a):
        print("iadd", a)
        return self
    def __add__(self, a):
        print("add", a)
        return self

obj = opSample() # obj = int() 비슷한 의미

obj += 10
obj + 10
10 + obj
print("----- 연산자 매직메서드 예시 끝 -----")






















