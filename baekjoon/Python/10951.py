# A+B - 4
'''
# 런타임 에러 (EOFError)
while True :
    A, B = map(int, input().split())
    print(A+B)
'''

try:
    while True:
        A, B = map(int, input().split())
        print(A+B)
except:
    exit()
