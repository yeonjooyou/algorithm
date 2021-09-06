# 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = str(input())

for x in croatia : # croatia 리스트의 각 원소가 string에 있다면 크로아티아 알파벳으로 인식
    string = string.replace(x, '#') # replace(문자, 대체문자)
    # print(string)

print(len(string))