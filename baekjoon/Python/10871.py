# X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))

num_list = []
for i in range(0, len(A)) :
    if A[i] < X :
        num_list.append(A[i])

for i in range(0, len(num_list)) :
    print(num_list[i], end=' ')