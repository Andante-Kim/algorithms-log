# 백준 1316 : 그룹 단어 체커

import sys

# get input word
num = int(input())

li = []
for _ in range(num):
  li.append(sys.stdin.readline().strip())

count = 0

alphabet_li = [0] * 26

for i in li:
  for j in range(len(i)):
    if j != (len(i)-1) and (i[j] == i[j+1]):
      continue
    else:
      alphabet_li[ord(i[j]) - 97] += 1

  if max(alphabet_li) < 2:
    count += 1
  alphabet_li = [0] * 26

print(count)