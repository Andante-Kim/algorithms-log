# 백준 4673: 셀프 넘버

li = [i for i in range(10001)]

def find_selfnum(li, num):
    next_num = num
    digit = [0, 0, 0, 0, 0]
    
    digit[4] = num//10000
    digit[3] = num//1000 - digit[4]*10
    digit[2] = num//100 - digit[3]*10 - digit[4]*100
    digit[1] = num//10 - digit[2]*10 - digit[3]*100 - digit[4]*1000
    digit[0] = num%10
    next_num += sum(digit)
    if next_num > 10000:
        return 0
    else:
        li[next_num] = 0
        return find_selfnum(li, next_num)

for k in range(10001):
    if li[k] == 0:
        continue
    else:
        find_selfnum(li, k)

for t in li:
    if t == 0:
        continue
    print(t)
