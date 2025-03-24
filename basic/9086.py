#백준: 9086 문자열

t = int(input())

for _ in range(t):
  test = input()
  print('{}{}'.format(test[0], test[-1]))