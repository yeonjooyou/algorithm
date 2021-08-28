# 평균은 넘겠지
C = int(input())
for _ in range(C) :
    case = list(map(int, input().split()))
    mean = sum(case[1:])//case[0]
    count = 0
    for i in range(1, len(case)) :
        if case[i] > mean :
            count += 1
    print('{:.3f}%'.format(count*100/case[0]))