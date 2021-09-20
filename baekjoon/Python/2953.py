# 나는 요리사다
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
A4 = list(map(int, input().split()))
A5 = list(map(int, input().split()))

sum_list = []
sum_list.append(sum(A1))
sum_list.append(sum(A2))
sum_list.append(sum(A3))
sum_list.append(sum(A4))
sum_list.append(sum(A5))

print(sum_list.index(max(sum_list))+1, max(sum_list))
# index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
