# OX퀴즈
T = int(input())
for _ in range(T) :
    result = list(str(input()))
    score = 0
    for i in range(0, len(result)) :
        if result[i] == 'O' :
            for j in range(1, len(result)-i) :
                if result[i+j] == 'O':
                    score += 1
                else :
                    break
            score += 1
    print(score)