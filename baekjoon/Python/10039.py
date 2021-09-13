# 평균 점수
sum = 0
for _ in range(1, 6) :
    score = int(input())
    if score < 40 :
        score = 40
    sum += score
print(int(sum/5))