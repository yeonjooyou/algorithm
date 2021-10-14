# 내 학점을 구해줘
import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    N = int(input())

    grade = 0
    sum = 0
    for _ in range(N) :
        C, G = map(float, sys.stdin.readline().split())
        grade += C
        sum += C*G
    print(int(grade), round(sum/grade, 1))