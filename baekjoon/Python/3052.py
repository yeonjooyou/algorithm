# 나머지
s = set()
for _ in range(1, 11) :
    num = int(input())
    s.add(num%42)
print(len(s))