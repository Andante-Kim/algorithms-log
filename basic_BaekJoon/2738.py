# 백준 2738 : 행렬 덧셈

import sys

n, m = map(int, sys.stdin.readline().split())

# matrix A
A = []
for _ in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    A.append(li)

# matrix B
B = []
for _ in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    B.append(li)


output = 0

for i in range(n):
    for j in range(m):
        output = A[i][j] + B[i][j]
        print(output, end=' ')
    print()