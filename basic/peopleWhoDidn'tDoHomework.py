import sys

std_li = [0] * 30

for _ in range(28):
  n = int(sys.stdin.readline())
  std_li[n-1] += 1

for k in range(30):
  if std_li[k] == 0:
    print(k + 1)