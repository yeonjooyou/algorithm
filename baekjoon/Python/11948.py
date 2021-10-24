# 과목선택
import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())
F = int(sys.stdin.readline())
science = [A, B, C, D]
science.sort()
society = [E, F]
society.sort()
del science[0], society[0]
print(sum(science)+sum(society))