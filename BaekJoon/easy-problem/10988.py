# 백준: 10988 팰린드롬인지 확인하기

a = input()
b = a[::-1]

if a == b:
  print(1)
else:
  print(0)