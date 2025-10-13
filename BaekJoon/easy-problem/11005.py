# 백준 11005 : 진법변환2

N, B = map(int, input().split())

i = 36
num = 0
result = []

while i >= 0:
  if B**i > N:
    i -= 1
    result.append(0)
  else:
    num = N // (B**i)
    N -= (B**i)*num
    if num > 9:
      result.append(chr(num + 55))
    else : 
      result.append(num)
    i -= 1

first = 0
for k in result:
  if k == 0:
    if first == 0:
      continue
    else:
      print(k, end="")
  else:
    first = 1
    print(k, end="")