# 백준 2581 : 소수

M = int(input())
N = int(input())

prime_num = []
for i in range(M, N+1):
    if i < 2:      # i가 1일 경우 소수에 포함되지 않음을 유의!
        continue
    divisor = False
    for k in range(2, i):
        if i%k == 0:
            divisor = True
            break
    if divisor == False:
        prime_num.append(i)

if len(prime_num) == 0:
    print(-1)
else:
    print(sum(prime_num))
    print(prime_num[0])
