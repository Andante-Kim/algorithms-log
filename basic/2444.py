# 백준: 2444 별 찍기-7

n = int(input())

for i in range(1,n+1):
  print(' ' * (n-i),end='')
  print('*' * i, end='')
  print('*' * (i-1))
  
for k in range(n-1, 0, -1):
  print(' ' * (n-k), end='')
  print('*' * k, end='')
  print('*' * (k-1))