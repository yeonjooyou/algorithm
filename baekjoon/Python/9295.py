# 주사위
T = int(input())
i = 0
for _ in range(T) :
    i += 1
    A, B = map(int, input().split())
    print('Case ', i, ': ', A+B, sep='')