# 한수
def hansu(num) :
    cnt = 0
    for i in range(1, num+1) :
        num_list = list(map(int, str(i)))
        if i < 100 : # 99이하의 자연수는 모두 한수
            cnt += 1
        elif num_list[1] - num_list[0] == num_list[2] - num_list[1] : # 한수 판별
            cnt += 1
    return cnt

num = int(input())
print(hansu(num))