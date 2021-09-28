# 사과
N = int(input())
num_list = []
sum = 0
for i in range(0, N) :
    num_list.append(list(map(int, input().split())))
    sum += num_list[i][1] % num_list[i][0]
# print(num_list)
print(sum)
'''
for i in range(0, N) :
    sum += num_list[i][1]%num_list[i][0]
print(sum)
'''