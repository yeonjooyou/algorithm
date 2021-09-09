# 달팽이는 올라가고 싶다
'''
# 시간초과 코드
A, B, V = map(int, input().split())
day = 1
H = A
while True :
    H += A-B
    day += 1
    if V <= H:
        break
print(day)
# 반복문을 돌리면 큰 숫자가 주어질 때 시간초과가 뜨므로 반복문은 지양해야한다.
'''

import math
A, B, V = map(int, input().split())
day = (V-B)/(A-B)
print(math.ceil(day))

# 반올림을 해주는 math.ceil() API를 사용한다.
# round() 사용 시 4.3->4, 4.6->5 (사사오입 원칙)
# math.ceil() : 올림, math.floor() : 내림, math.trunc() : 버림