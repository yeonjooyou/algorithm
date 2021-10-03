# 지능형 기차 2
import sys
num_list = []
for _ in range(10) :
    num_list.append(list(map(int, sys.stdin.readline().split())))

sum = 0
sum_list = []
for i in range(0, len(num_list)):
    sum += (-1) * num_list[i][0]
    sum_list.append(sum)
    sum += num_list[i][1]
    sum_list.append(sum)
print(max(sum_list))