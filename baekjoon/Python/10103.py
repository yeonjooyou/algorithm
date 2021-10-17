# 주사위 게임
n = int(input())
CY_score = 100
SD_score= 100
for _ in range(n) :
    CY, SD = map(int, input().split())
    if CY > SD :
        SD_score -= CY
    elif CY < SD :
        CY_score -= SD
    else :
        pass
print(CY_score)
print(SD_score)