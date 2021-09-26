# 인공지능 시계
A, B, C = map(int, input().split())
D = int(input())

C += D%60
if C >= 60 :
    C -= 60
    B += 1

D //= 60
B += D%60
if B >= 60 :
    B -= 60
    A += 1

D //= 60
A += D%24
if A >= 24 :
    A -= 24

print(A, B, C)

# 틀린 코드
# print((A + (B+D//60)//60)%24, (B + (C+D)//60%60)%60, (C + D%60)%60)