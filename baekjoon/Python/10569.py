# 다면체 : 꼭짓점 - 모서리 + 면 = 2
T = int(input())
for _ in range(T) :
    V, E = map(int, input().split()) # 꼭짓점, 모서리
    print(2 - V + E)