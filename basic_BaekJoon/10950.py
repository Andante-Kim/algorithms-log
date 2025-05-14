t = int(input())
li = []

for _ in range(t):
  a, b = map(int, input().split())
  li.append([a, b])

for k in li:
  print(k[0] + k[1])
