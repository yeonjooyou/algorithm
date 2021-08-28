# 평균
N = int(input())
# 파이썬에서 리스트로 한 줄에 여러 값 입력받는 방법
score_list = list(map(int, input().split()))
# 최댓값 찾은 후 list의 값 바꾸기
M = max(score_list)
for i in range(0,N) :
    score_list[i] = score_list[i]/M*100
# 평균구하기
sum=0
for i in range(0, N) :
    sum += score_list[i]
print(sum/N)
