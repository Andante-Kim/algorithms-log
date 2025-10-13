# 백준 2480 : 주사위 세개

li = []
num = 0

li.extend(map(int, input().split())) 

count_li = [0] * 7

for i in li:
  count_li[i] += 1

max_num = max(count_li)

if max_num == 3:
  num = 10000 + (count_li.index(3) * 1000)
elif max_num == 2:
  num = 1000 + (count_li.index(2) * 100)
else:
  num = max(li) * 100

print(num)
