# 대표값2
import sys
num_list = []
for _ in range(5) :
    num_list.append(int(sys.stdin.readline()))
print(sum(num_list)//5) # 평균
mid = sorted(num_list)
print(mid[2]) # 중앙값