# 지능형 기차
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
C1, C2 = map(int, input().split())
D1, D2 = map(int, input().split())

num_list = [A1, A2, B1, B2, C1, C2, D1, D2]

sum = 0
sum_list = []
for i in range(0, len(num_list)):
    sum += (-1)**(i+1)*num_list[i]
    sum_list.append(sum)
print(max(sum_list))
