# 시험 점수
min = list(map(int, input().split()))
man = list(map(int, input().split()))
S = sum(min)
T = sum(man)
if S >= T :
    print(S)
else :
    print(T)