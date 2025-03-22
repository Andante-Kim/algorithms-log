import sys

n, m = map(int, sys.stdin.readline().split())
basket_n = [0] * (n+1)

for _ in range(m):
  i, j, k = map(int, sys.stdin.readline().split())
  for a in range(i, j+1):
    basket_n[a] = k

print(*basket_n[1:])