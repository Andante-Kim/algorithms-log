li = []

for _ in range(9):
  li.append(int(input()))

max_li = max(li)

print(max_li)
print(li.index(max_li) + 1)
