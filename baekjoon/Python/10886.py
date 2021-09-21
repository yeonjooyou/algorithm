# 0 = not cute / 1 = cute
N = int(input())

cute = 0
notcute = 0
for i in range(1, N+1) :
    opinion = int(input())
    if opinion == 1 :
        cute += 1
    elif opinion == 0 :
        notcute += 1

if cute > notcute :
    print('Junhee is cute!')
else :
    print('Junhee is not cute!')