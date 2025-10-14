# 백준 10773: 제로
import sys

k = int(input())
li = []

for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        li.pop()
    else:
        li.append(num)

print(sum(li))

