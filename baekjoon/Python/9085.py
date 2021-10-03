# 더하기
import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    print(sum(num_list))