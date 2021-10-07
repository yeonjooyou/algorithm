# 수도요금
import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
P = int(sys.stdin.readline())

case1 = A*P
if P <= C :
    case2 = B
else :
    case2 = B + (P-C)*D

if case1 <= case2 :
    print(case1)
else :
    print(case2)