# 5와 6의 차이
A, B = map(str, (input().split()))
min = int(A.replace('6','5')) + int(B.replace('6', '5')) # replace() : 문자열의 특정값을 변환
max = int(A.replace('5','6')) + int(B.replace('5', '6'))
print(min, max)