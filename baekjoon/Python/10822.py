# 더하기
S = list(map(int, input().split(',')))
sum = 0
for i in range(len(S)) :
    sum += S[i]
print(sum)