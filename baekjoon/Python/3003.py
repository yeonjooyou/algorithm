# 킹, 퀸, 룩, 비숍, 나이트, 폰
import sys
find_list = list(map(int, sys.stdin.readline().split()))

chess_list = [1, 1, 2, 2, 2, 8]
for i in range(0, len(find_list)) :
    print(chess_list[i] - find_list[i], end=' ')