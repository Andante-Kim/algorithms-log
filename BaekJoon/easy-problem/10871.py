n, x = map(int, input().split())

n_li = []

n_li.extend(map(int, input().split()))

for i in n_li:
  if i < x:
    print(i,end=' ')
