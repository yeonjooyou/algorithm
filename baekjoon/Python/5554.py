# 심부름 가는 길
import sys
sum = 0
for _ in range(4) :
    sum += int(sys.stdin.readline())

x = sum // 60
y = sum % 60

print(x)
print(y)