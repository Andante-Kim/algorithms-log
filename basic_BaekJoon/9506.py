# 백준 9506 : 약수들의 합

n = int(input())

while n != -1 :
    # find divisors
    divisor = []
    for i in range(1, n):
        if n%i == 0:
            divisor.append(i)
    
    if sum(divisor) == n:
        print(n, '=', end=' ')
        for k in range(len(divisor)-1):
            print(divisor[k],'+',end=' ')
        print(divisor[-1])
    else:
        print(n, 'is NOT perfect.')
        
    n = int(input())
