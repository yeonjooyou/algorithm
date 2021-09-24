# 파티가 끝나고 난 뒤
L, P = map(int, input().split())
fake = list(map(int, input().split()))

fact = []
for i in range(0, len(fake)) :
    fact.append(fake[i] - L*P)

for i in range(0, len(fact)):
    print(fact[i], end=' ')