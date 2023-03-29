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

print("----- 문자열 작업 등 제어2 예시 끝 -----")

# 리스트 자료구조 제어
a = [1,2,3,4,5,6,7]
print(a)
a[2] = 10
print(a)

del a[1]
print(a)
del a[3:] # idx 3 끝까지 삭제
print(a)
a.append(999)
#a.append([111,222,33])
print(a)
a.extend([111,222,333,111])
print(a)
a.sort() # sorted() 정렬한 새로운 리스트 생성
print(a)

print(a.reverse() or a)
print(a.insert(0, 10) or a)
print(a.remove(999) or a) #999값을 찾아서 삭제
print(a.pop() and a)    # 끝위치 값을 꺼내고 삭제
print(a.pop(0) and a)   # 0위치 값을 꺼내고 삭제 

print(a.count(111))     # 111과 같은 값을 카운팅
print(a * 3)

print("----리스트 예시 끝----")


# 튜플 자료구조 제어
a = (1,2,3,4,5,6,7)
print(a)
#a[2] = 10
#print(a)

#del a[1]
#print(a)
#del a[3:] # idx 3 끝까지 삭제
#print(a)
#a.append(999)
#a.append([111,222,33])
#print(a)
#a.extend([111,222,333,111])
#print(a)
#a.sort() # sorted() 정렬한 새로운 리스트 생성
#print(a)

#print(a.reverse() or a)
#print(a.insert(0, 10) or a)
#print(a.remove(999) or a) #999값을 찾아서 삭제
#print(a.pop() and a)    # 끝위치 값을 꺼내고 삭제
#print(a.pop(0) and a)   # 0위치 값을 꺼내고 삭제 

print(a.count(111))     # 111과 같은 값을 카운팅
print(a * 3)

print("----튜플 예시 끝----")

#사전 자료구조
dict1 = {"name":"hong", "age":20, "email":["abc@naver.com", "sec@naver.com"],
         34:"numvalue", (1,2) : "tuplevalue", 1.2 : "float_value"}
dict2 = dict1 #참조복사
print(dict1)

dict1 = {"new" : 999 } # 새로운 딕셔너리 만들어서 할당
dict1["new1"] = 998
dict1[55] = (999, 222)
print(dict1)

del dict1["new"]
del dict1[55]
print("-------")

dict1 = dict2 #참조복사

#key 값을 순회 추출
for x in dict1.keys(): #dict1만 입력하는 것과 같음
    print(x) 

#values 값을 순회 추출
for x in dict1.values():
    print(x)

#(key, value)
for x in dict1.items():
    print(x)

#zip, enumerate

#값을 접근하는 방법
print(dict1["name"])  # dict1.setdefault(키이름, 값) => 만일 기존 키가 있을경우 기존 값 리턴 
print(dict1.get("name1"))  # 해당 key가 없을 경우 예외처리 하지 않고 None 리턴
print(dict1.get("name1", "empty")) # key가 없을 경우 기본값 리턴

#deepcopy/swallow 복사
dict3 = dict2.copy() #swallow

import copy
dict4 = copy.deepcopy(dict2) #deepcopy

dict2["email"][0] = "new@naver.com"

print("-----copy----")
print(dict2)
print("-----dict3----")
print(dict3)
print("-----dict4 deep----")
print(dict4)

print(dict2.clear() or dict2)


print("-----사전 사용 예시----")



#set
set1 = {1,2,3,3,4}
set2 = set((3,4,5,6))
print(set1)
print(set2)

print(set1 & set2) #교집합
print(set1.intersection(set2))

print(set1 | set2) #합집합
print(set1.union(set2))

print(set1 - set2) #차집합
print(set1.difference(set2))

print(set1 ^ set2) #합집합 - 교집합

print(set1.add(100) or set1)
print(set1.update([11,22,33]) or set1)

print(set1.remove(11) or set1)















    

















































































      
















