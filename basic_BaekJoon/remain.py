import sys

remain = set()

for _ in range(10):
  i = int(sys.stdin.readline())
  remain.add(i%42)

remain = list(remain)
print(len(remain))