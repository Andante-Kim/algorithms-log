import sys

t = int(input())
for _ in range(t):
  r, s = map(str, sys.stdin.readline().split())
  for i in s:
    print(i*int(r), end='')
  print()