# 백준 9063 : 대지

import sys

n = int(sys.stdin.readline())
li = []
x_li = []
y_li = []

for _ in range(n):
    dot = list(map(int, sys.stdin.readline().split()))
    li.append(dot)
    x_li.append(dot[0])
    y_li.append(dot[1])

land_y = max(y_li) - min(y_li)
land_x = max(x_li) - min(x_li)   

print(land_x * land_y)
