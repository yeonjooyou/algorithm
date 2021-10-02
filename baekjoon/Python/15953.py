# 상금 헌터
import sys

a_prize = [500, 300, 200, 50, 30, 10]
b_prize = [512, 256, 128, 64, 32]

T = int(sys.stdin.readline())
for _ in range(1, T+1) :
    a, b = map(int, sys.stdin.readline().split())
    prize = 0
    if a == 1 : # 1등
        prize += a_prize[0]
    elif 2 <= a <= 3 : # 2등
        prize += a_prize[1]
    elif 4 <= a <= 6 : # 3등
        prize += a_prize[2]
    elif 7 <= a <= 10 : # 4등
        prize += a_prize[3]
    elif 11 <= a <= 15 : # 5등
        prize += a_prize[4]
    elif 16 <= a <= 21 : # 6등
        prize += a_prize[5]

    if b == 1 : # 1등
        prize += b_prize[0]
    elif 2 <= b <= 3 : # 2등
        prize += b_prize[1]
    elif 4 <= b <= 7 : # 3등
        prize += b_prize[2]
    elif 8 <= b <= 15 : # 4등
        prize += b_prize[3]
    elif 16 <= b <= 31 : # 5등
        prize += b_prize[4]
    print(prize*10000)