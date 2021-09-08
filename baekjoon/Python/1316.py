# 그룹 단어 체커
N = int(input())
group_word = N
for _ in range(N) :
    word = list(input())
    for i in range(0, len(word)-1) :
        if word[i] == word[i+1] :
            pass
        elif word[i] in word [i+1:] :
            group_word -= 1
            break
print(group_word)