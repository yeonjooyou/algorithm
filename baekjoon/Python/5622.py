# 다이얼
string = list(str(input()))

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for i in range(0, len(string)) :
    for j in dial : # j는 다이얼 리스트의 원소
        if string[i] in j :
            time += dial.index(j) + 3

print(time)