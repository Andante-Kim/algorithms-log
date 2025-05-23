# 백준 24265 : 알고리즘 수업 - 알고리즘의 수행시간4

n = int(input())

print(int((n-1)*n/2))
print(2)

'''
변수 i는 1부터 (n-1)까지 수행됩니다. 따라서

i = 1 일 때, j = 2 ~ n : #코드 (n-1)번 수행

i = 2 일 때, j = 3 ~ n : #코드 (n-2)번 수행

.....

i = n-2 일 때, j = n-1 ~ n : #코드 2번 수행

i = n-1 일 때, j= n ~ n : #코드 1번 수행

따라서 총 실행 횟수는 1+2+...+(n-2)+(n-1) 이고, 이를 수열 공식에 적용하면

(n-1){1 + (n-1)} / 2 = (n-1)n / 2가 됩니다.

따라서 n에 따른 #코드의 수행횟수는 위 식을 적용하면 되고, 최고차항의 차수는 항상 2가 됩니다!
'''
