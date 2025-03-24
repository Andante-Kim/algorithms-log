#백준: 10813 공 바꾸기

import sys

n, m = map(int, sys.stdin.readline().split())

basket_li = [(k+1) for k in range(n)]

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  basket_li[i-1], basket_li[j-1] = basket_li[j-1], basket_li[i-1]

print(*basket_li)