# 백준 11047: 동전 0

N, K = map(int, input().split()) # 동전 종류 N, 원하는 합 K
A = [] # 동전의 가치
need_c = 0 # 필요한 동전의 개수

for _ in range(N):
    c = int(input())
    A.append(c)
A.sort(reverse=True)

for v in range(N):
    num = K//A[v]
    K -= A[v]*num
    need_c += num
    
    if N == 0:
        break

print(need_c)