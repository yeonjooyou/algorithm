# 배수 찾기
n = int(input())
while True :
    num = int(input())
    if num == 0 :
        break
    elif num % n == 0 :
        print(num, ' is a multiple of ', n, '.', sep='')
    else :
        print(num, ' is NOT a multiple of ', n, '.', sep='')