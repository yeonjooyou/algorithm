# 점수계산
import sys
N = int(sys.stdin.readline())
correct = list(map(int, sys.stdin.readline().split()))

score = []
for i in range(0, N) :
    if correct[i] == 1 :
        score.append(1)
    else :
        score.append(0)

final = 0
for i in range(0, N) :
    if score[i] == 1 :
        for j in range(1, N-i) :
            if score[i+j] == 1:
                final += 1
            else :
                break
        final += 1
print(final)