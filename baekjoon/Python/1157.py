# 단어 공부
word = str(input()).upper() # 출력값이 대문자이므로 입력받은 문자열을 모두 대문자로 바꿈

word_list = list(set(word)) # 입력받은 문자열의 중복값 제거->set()
# print(word_list)
cnt_list = [] # word의 각 문자열 갯수를 저장할 리스트
for x in word_list :
    cnt_list.append(word.count(x))

if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    print(word_list[cnt_list.index(max(cnt_list))])
    # cnt_list의 최댓값의 위치를 반환하여 word_list에 인덱싱하여 해당 문자열 반환