# 주사위 세개
A, B, C = map(int, input().split())

dice_list = [0, 0, 0, 0, 0, 0]
dice_list[A-1] += 1
dice_list[B-1] += 1
dice_list[C-1] += 1

one_list = []
if 3 in dice_list :
    print(10000 + (dice_list.index(3)+1)*1000)
elif 2 in dice_list :
    print(1000 + (dice_list.index(2)+1)*100)
else :
    for i in range(6) :
        if dice_list[i] == 1 :
            one_list.append(i+1)
    print(max(one_list)*100)