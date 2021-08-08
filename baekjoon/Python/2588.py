# 곱셈
num1 = int(input())
num2 = int(input())

a = num1 * (num2%10)
b = num1 * (num2%100 - num2%10) / 10
c = num1 * (num2 - num2%100) / 100

print(int(a))
print(int(b))
print(int(c))
print(int(a+b*10+c*100))