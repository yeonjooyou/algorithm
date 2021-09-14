# 검증수
num_list = list(map(int, input().split()))

sum = 0
for i in range(0, len(num_list)) :
    sum += num_list[i]**2
print(sum%10)