# 셀프 넘버
def d(n) :
    n = n + sum(map(int, str(n)))
    return n

nature = set(range(1, 10001))
generator = set()
for i in range(1, 10001) :
    generator.add(d(i))

self_number = sorted(nature - generator)
for i in self_number :
    print(i)