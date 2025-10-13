# 백준 2292 : 벌집

N = int(input())

route = 0
count = 0
i = 0

N -= 1

while 1:
    if N <= 6*i:
        break
    else:
        count += 1
        i += count

print(count + 1)
