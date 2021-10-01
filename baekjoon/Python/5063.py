# TGN
N = int(input())

case = []
for i in range(0, N) :
    case.append(list(map(int, input().split())))
    if case[i][0] < case[i][1]-case[i][2] :
        print('advertise')
    elif case[i][0] == case[i][1]-case[i][2] :
        print('does not matter')
    else :
        print('do not advertise')