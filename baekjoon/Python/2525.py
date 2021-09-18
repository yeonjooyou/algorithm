# 오븐 시계
A, B = map(int, input().split())
C = int(input())
if B+C >= 60 :
    print((A+(B+C)//60)%24, (B+C)%60)
else :
    print(A%24, B+C)