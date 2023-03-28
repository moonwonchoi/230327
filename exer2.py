datas = "s88,39,33es12,33,45es33,32s13,77,45es33,55,66e"

temp = []
spd = []
weg = []

found_s_idx = 0
found_e_idx = 0

s_idx = datas.index("s", found_s_idx)
e_idx = datas.index("e", found_e_idx)

found_s_idx = s_idx + 1
found_e_idx = e_idx + 1

data = datas[s_idx + 1 : e_idx]

values = data.split(",")

temp.append(int(values[0]))
spd.append(int(values[1]))
weg.append(int(values[2]))


#평균값: 온도: 36.5 속도: 51.0 중량: 47.25

#반복
#s / e규칙
#, 값을 추출
# 저장다하고 평균


#s위치를 찾고, 그다음 e의 위치를 찾는 그런 메소드가 없을까?
#.index("s", 0) -> 0
#.index("e", 0) -> 10
#[1:10] -> 추출
#88,39,33
#.split


