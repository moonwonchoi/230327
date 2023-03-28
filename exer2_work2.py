datas = "s88,39,33es12,33,45es33,32s13,77,45es33,55,66e"
#88,39,33
#12,33,45
# 33,32 에러
#13,77,45
#33,55,66
found_s_idx = 0
found_e_idx = 0
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
        found_s_idx = s_idx + 1
        found_e_idx = e_idx + 1
    
    if len(datas) <= found_e_idx:
        break

print("완료")







#평균값: 온도: 36.5 속도: 51.0 중량: 47.25

