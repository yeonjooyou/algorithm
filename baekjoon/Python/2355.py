# 시그마
import sys
A, B = map(int, sys.stdin.readline().split())
max = max(A, B)
min = min(A, B)
sum = (A + B) * (max - min + 1) / 2
print(int(sum))