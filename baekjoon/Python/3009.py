# 네 번째 점
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

if a1 == b1 :
    d1 = c1
elif a1 == c1 :
    d1 = b1
elif b1 == c1 :
    d1 = a1

if a2 == b2 :
    d2 = c2
elif a2 == c2 :
    d2 = b2
elif b2 == c2 :
    d2 = a2

print(d1, d2)

# case 2
x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]

print(x, y)