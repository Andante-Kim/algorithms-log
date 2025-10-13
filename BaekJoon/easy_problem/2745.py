# 백준 2745 : 진법 변환

# B진법 수 N
N, B = map(str,input().split())
B = int(B)

total = 0
line = 0
for i in N[::-1]:
  if i.isalpha():
    num = (ord(i)-65+10) * (B**line)
  else:
    num = int(i) * (B**line)
  total += num
  line += 1

print(total)
