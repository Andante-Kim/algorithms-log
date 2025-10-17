# 백준 11399: ATM

'''
인출하는데 필요한 시간의 합의 최솟값 공식
 :시간이 짧게 걸리는 사람일 수록 먼저!
'''

N = int(input()) # 사람의 수 N 입력
P = list(map(int, input().split())) # 각 사람이 돈을 인출하는데 걸리는 시간 P 입력
P.sort()
wait_time= 0
result = 0

for i in range(len(P)):
    wait_time += P[i]
    result += wait_time

print(result)