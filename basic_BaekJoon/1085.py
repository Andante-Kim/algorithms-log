# 백준 1085 : 직사각형에서 탈출

x, y, w, h = map(int, input().split())

length = [x, h-y, w-x, y]

print(min(length))
