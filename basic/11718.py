# 백준: 11718 그대로 출력하기

import sys

li = []

for _ in range(100):
  i = sys.stdin.readline().strip()
  if len(i) == 0:
    break
  else:
    li.append(i)

for l in li:
  print(l)