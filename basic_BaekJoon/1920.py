n = int(input())
li_n = set(map(int, input().split()))
m = int(input())
li_m = list(map(int, input().split()))

for i in li_m:
  print(1) if i in li_n else print(0)
