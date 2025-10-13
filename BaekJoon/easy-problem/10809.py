s = str(input())

alphabet_li = [-1] * 26
count = 0

for i in s:
  int_s = ord(i)
  if alphabet_li[int_s-97] == -1:
    alphabet_li[int_s-97] = count
  count += 1

print(*alphabet_li)
