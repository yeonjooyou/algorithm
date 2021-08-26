# 숫자의 개수
A = int(input())
B = int(input())
C = int(input())

lst = list(map(int, str(A*B*C)))
num_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, len(lst)) :
    num_lst[lst[i]] += 1

for i in range(0, len(num_lst)) :
    print(num_lst[i])