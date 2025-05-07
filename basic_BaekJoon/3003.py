# 백준: 3003 킹,퀸,룩,비숍,나이트,폰

origin = [1,1,2,2,2,8]

now = []
now.extend(map(int, input().split()))

for n in range(6):
  print(origin[n] - now[n], end=' ')