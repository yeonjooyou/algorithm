# 주사위 게임
N = int(input())
output = 0
for _ in range(N) :
    a, b, c = map(int, input().split())
    if a == b == c :
        output = max(output, 10000 + a * 1000)
    elif a == b:
        output = max(output, 1000 + a * 100)
    elif a == c:
        output = max(output, 1000 + a * 100)
    elif b == c :
        output = max(output, 1000 + b * 100)
    else :
        output = max(output, 100 * max(a, b, c))
print(output)