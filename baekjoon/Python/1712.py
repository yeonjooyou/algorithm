# 손익분기점
import sys
A, B, C = map(int, sys.stdin.readline().split())
if B >= C:
    print(-1)
else :
    print(int(A/(C-B))+1)
'''
# A,B,C 숫자가 작을 때
num = 0
while True :
    if B>=C :
        print(-1)
        break
    elif A + (B-C)*num >= 0 :
        num += 1
    else:
        print(num)
        break
'''