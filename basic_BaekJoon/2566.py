# 백준 2566 : 최댓값

import sys

li = []
max_num = [0, 0, 0] # max_num, index
k = 0
for i in range(9):
  m = list(map(int,sys.stdin.readline().split()))
  li.append(m)

  k = max(m)
  if k > max_num[0]:
    max_num[0] = k
    max_num[1] = i
    max_num[2] = m.index(k)

print(max_num[0])
print(max_num[1]+1, max_num[2]+1)
