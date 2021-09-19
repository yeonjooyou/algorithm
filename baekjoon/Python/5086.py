# 배수와 약수
while True :
    A, B = map(int, input().split())
    if A == 0 :
        break
    else :
        if A % B == 0 :
            print("multiple")
        elif B % A == 0 :
            print("factor")
        elif A % B != 0 and B % A != 0 :
            print("neither")