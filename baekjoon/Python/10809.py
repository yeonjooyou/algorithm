# 알파벳 찾기
S = list(input())
spot_list = []
for _ in range(26) :
    spot_list.append(-1)
for i in range(0, len(S)) :
    string = ord(S[i])-97
    if spot_list[string] == -1 :
        spot_list[string] = i

for i in range(0, len(spot_list)) :
    print(spot_list[i])