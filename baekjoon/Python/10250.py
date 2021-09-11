# ACM 호텔
T = int(input())
for _ in range(T) :
    H, W, N = map(int, input().split()) # 층 수, 방 수, 손님 순서
    if N%H == 0 :
        print(H * 100 + N // H)
    else :
        print((N % H) * 100 + (N // H) + 1)