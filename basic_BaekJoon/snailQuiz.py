a, b, v = map(int, input().split())

now_v = 0
day = 0

if a != v:
  day = (v-a) // (a-b)
  now_v = day * (a-b)


while 1:
  day += 1
  now_v += a
  
  if now_v >= v:
    break

  now_v -= b

print(day)