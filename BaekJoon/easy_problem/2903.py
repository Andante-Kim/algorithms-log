# 백준 2903 : 중앙 이동 알고리즘

# N : the number of processes
N = int(input())

# Let's calculte how many dots we should store!
# 0 : 2, 1 : 3, 2 : 5, 3 : 9

li = [2]
for i in range(1,16):
    num = li[i-1]
    li.append(num + (num-1))

print(li[N]**2)
