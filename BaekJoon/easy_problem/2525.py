a, b = map(int, input().split())
c = int(input())

# 요리 시간 더하기
b += c

# 시간 정리
hour = b // 60
a += hour
b -= hour*60

# 시 정리
if a >= 24:
  a -=24

print(a, b)
