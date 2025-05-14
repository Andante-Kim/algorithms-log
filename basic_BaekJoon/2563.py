# 백준 2563 : 색종이
import sys

big_paper = [[0]*100 for _ in range(100)]

num = int(sys.stdin.readline())
for _ in range(num):
  a, b = map(int, sys.stdin.readline().split())
  for n in range(b,b+10):
    for m in range(a,a+10):
      big_paper[n][m] = 1

sum_all = 0
for i in range(100):
  sum_all += sum(big_paper[i])
