#백준: 10811 바구니 뒤집기

import sys

n, m = map(int, sys.stdin.readline().split())

basket_li = [(k+1) for k in range(n)]

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  if i == 1:
    basket_li[:j] = basket_li[j-1::-1]
  else:
    basket_li[i-1:j] = basket_li[j-1:i-2:-1]

print(*basket_li)