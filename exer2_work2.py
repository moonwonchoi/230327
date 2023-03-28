fobj = open("data.txt", "r")
readfile = fobj.read()
print(readfile)
print("파일 읽기완료")
datas = readfile
#88,39,33
#12,33,45
# 33,32 에러
#13,77,45
#33,55,66
found_s_idx = 0
found_e_idx = 0

listtemp = []
listspd = []
listweg = []

while True:    
    s_idx = datas.index("s", found_s_idx)
    s_second_idx = datas.find("s", s_idx + 1)    
    e_idx = datas.index("e", found_e_idx)
    
    #print(s_idx, s_second_idx, e_idx)

    if s_second_idx < e_idx and s_second_idx != -1:
        # 비정상
        found_s_idx = s_second_idx
    else:
        print(datas[s_idx+1:e_idx]) # 정상
        rawdata = datas[s_idx+1:e_idx]    #"abcde" [1:3] -> "bc"
        rawlist = rawdata.split(",") #"33,44,55" # -> ["33", "44", "55"]
        listtemp.append(int(rawlist[0]))
        listspd.append(int(rawlist[1]))
        listweg.append(int(rawlist[2]))
        found_s_idx = s_idx + 1
        found_e_idx = e_idx + 1
    
    if len(datas) <= found_e_idx:
        break

print("완료")

print(listtemp, sum(listtemp), len(listtemp))
print(listspd, sum(listspd), len(listspd))
print(listweg, sum(listweg), len(listweg))


disp_text = f"평균값: 온도: {sum(listtemp) / len(listtemp)} 속도: {int(sum(listspd) / len(listspd))} 중량: {sum(listweg) / len(listweg)}"

print(disp_text)
