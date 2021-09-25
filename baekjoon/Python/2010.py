# 플러그
import sys
N = int(sys.stdin.readline())

plug = 0
for _ in range(1, N+1) :
    num = int(sys.stdin.readline())
    plug += num-1
print(plug+1)
'''
# 시간초과
# input() vs. sys.stdin.readline() : input()은 prompt message를 출력하고 개행문자를 삭제한 값을 리턴
plug = 0
for _ in range(1, N+1) :
    num = int(input())
    plug += num-1
print(plug+1)
'''