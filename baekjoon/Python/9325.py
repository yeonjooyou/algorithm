# 얼마?
T = int(input())
for _ in range(T) :
    s = int(input())
    n = int(input())
    sum = 0
    for _ in range(n) :
        q, p = map(int, input().split())
        sum += q * p
    print(s + sum)