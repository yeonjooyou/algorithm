# 최소공배수
T = int(input())
for _ in range(T) :
    A, B = map(int, input().split())
    '''
    for i in range(max(A, B), A*B+1) :
        if i%A == 0 and i%B == 0 :
            print(i)
            break
    '''
    # gcd() : 재귀함수
    def gcd(a, b):
        return gcd(b, a % b) if b else a
    def lcm(a, b):
        return a * b // gcd(a, b)
    print(lcm(A, B))