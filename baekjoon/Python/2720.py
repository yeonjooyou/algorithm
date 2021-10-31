# 세탁소 사장 동혁
T = int(input())
for _ in range(T) :
    C = int(input())
    Q = C // 25
    C -= 25*Q
    D = C // 10
    C -= 10*D
    N = C // 5
    C -= 5*N
    P = C // 1
    print(Q, D, N, P)