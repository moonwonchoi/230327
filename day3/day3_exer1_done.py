#최대값
#최대값 구할려고, 값들 어떻게 구성할지
# 12 6 18
# -> 배열 (시퀀스), 그냥 각각 변수로 구성할건지
# -> for + if, 모든 변수들을 조건문으로 작성해서 최대값을 찾아야지

a = 12
b = 6
c = 18

maxnum = a
if a > b:
    if a > c:
        maxnum = a
    else:
        maxnum = c

else:
    if b > c:
        maxnum = b
    else:
        maxnum = c

print("maxnum:", maxnum)




listvar = [12, 6, 18]
loopmax = listvar[0]
for get in listvar:
    if get > loopmax:
        loopmax = get

print("최대값:", loopmax)



for step1 in range(2,10):
    print(step1,"단:", sep="", end="")

    for step2 in range(1,10):
        #print(step1, "*", step2, "=", step1 * step2, sep="", end="\t")
        print(f"{step1}*{step2}={step1*step2}", end="\t")

    print("\n")






























