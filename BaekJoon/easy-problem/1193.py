# 백준 1193 : 분수 찾기

X = int(input())

count = 1
k = 1
past = 0
while 1:
    if k >= X:
        break
    else:
        past += count
        count += 1
        k += count

new_X = X - past - 1

li = []
a, b = 1, count
while a <= count:
    li.append([a, b])
    a += 1
    b -= 1


new_li = li[new_X]
if count%2 == 0:
    print("{}/{}".format(new_li[0], new_li[1]))
else:
    print("{}/{}".format(new_li[1], new_li[0]))
