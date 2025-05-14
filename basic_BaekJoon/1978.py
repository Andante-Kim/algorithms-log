n = int(input())

li = []
li.extend(map(int, input().split()))

count = 0

for k in li:
  if k != 1:
    count += 1
  for a in range(2, k-1):
    if k%a == 0:
      count -= 1
      break

print(count)
