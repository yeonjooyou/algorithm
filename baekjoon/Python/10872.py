# 팩토리얼
# case1. 재귀함수 사용
N = int(input())
def factorial(n) :
    if n > 1 :
        return n*factorial(n-1)
    else :
        return 1
print(factorial(N))

# case2. math 라이브러리 사용
import math
N = int(input())
print(math.factorial(N))