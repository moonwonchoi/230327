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


#문자열 및 시퀀스타입 길이 구하기
v_seq_str = "abcde"
v_seq_list = [1,2,3,4]
v_seq_tuple = (1,2,3,4)
print(len(v_seq_str), len(v_seq_list), len(v_seq_tuple))

#dict
# { "name" : "choi", "age" : 11}
print(len(v_dict1), len(v_dict1.keys()), len(v_dict1.values())) #같은 의미(keys())

print("----- 길이구하기 예시 끝 -----")

#슬라이싱  [:]
print(v_seq_str[:]) #첫 위치부터 끝 위치까지   - 슬라이싱 
print(v_seq_str[-1::-1]) # 끝위치부터 첫 위치까지 (역순)   - 확장슬라이싱
               #[시작위치 : 종료위치 : 증감]
print(v_seq_str[::2]) #첫 위치부터 끝 위치까지 2칸 간격 씩

print("----- 슬라이싱 예시 끝 -----")

#특정문자수 카운팅, 위치 찾기
v_str_count = "aaabbbccccc"
print(v_str_count.count("b"))
print(v_str_count.index("b"), v_str_count.find("b")) #문자 위치 찾기
#.index 없을 경우 예외발생, find는 return값으로 -1

print("----- 문자카운팅 위치 찾기 예시 끝 -----")

#문자 삽입, 대소문자변환, 공백 삭제
v_join_str = "python"
print(".".join(v_join_str)) # p.y.t.h.o.n
v_case = "PyThOn"
print(v_case.upper())
print(v_case.lower())
v_space_str = " P YTHO N "
print(v_space_str.strip())  #시작 / 끝 공백 제거 (내부 제외)
print(v_space_str.lstrip()) #시작 공백제거 
print(v_space_str.rstrip()) #끝 공백 제거

#문자열 나누기
print(v_space_str.split(" ")) #' ' 일반적으로 앞뒤 공백 제거 후 split 

print("----- 문자열 사업 등 제어2 예시 끝 -----")






























      
















