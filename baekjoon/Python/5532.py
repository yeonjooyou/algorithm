# 방학 숙제
import sys
L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

if A%C == 0 :
    kor = A//C
elif A%C != 0 :
    kor = A//C + 1
if B%D == 0 :
    math = B//D
elif B%D != 0 :
    math = B//D + 1

if kor>math :
    print(L-kor)
else :
    print(L-math)