# 숫자의 합
N = int(input())
nums = str(input())
num_list = list(map(int, str(nums)))
print(sum(num_list))

'''
# case2. 입력받은 N을 이용하는 경우
sum = 0
for i in range(0, N) :
    sum += num_list[i]
print(sum)
'''