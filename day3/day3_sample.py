subjects = ['math', 'history', 'english', 'computer engineering','test']
scores = [90, 80, 95, 100]

# 이 코드가 아래 한줄로 표현됨 
score_dict = dict()
for key, value in zip(subjects, scores):
    score_dict[key] = value
print(score_dict)

score_dict = {key:value for key,value in zip(subjects, scores)}
print(score_dict)

# enumerate 를 안쓸경우
idx = 0
for y in subjects:    
    if len(scores) > idx:
        print(y, "," , scores[idx])
    else:
        print(y, "," , "점수없음")
    idx = idx + 1

print("-------------")

# (0, "math") ~~~~
for x,y in enumerate(subjects):
    if len(scores) > x:
        print(y, "," , scores[x])
    else:
        print(y, "," , "점수없음")

print("-------------")

# ("math", 90) ~~~~~~
for x, y in zip(subjects, scores):  #[('math', 90), ~~~]
    print(x)
    print(y)

