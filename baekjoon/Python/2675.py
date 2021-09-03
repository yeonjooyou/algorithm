# 문자열 반복
T = int(input())
for _ in range(T) :
    case = list(map(str, input()))
    for i in range(2, len(case)) :
        print(case[i]*int(case[0]), end='')
    print()