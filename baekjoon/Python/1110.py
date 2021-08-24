# 더하기 사이클
N = int(input())

num = N
len = 0
while True :
    num = (num % 10) * 10 + (num // 10 + num % 10) % 10
    len += 1
    if num == N :
        break
print(len)