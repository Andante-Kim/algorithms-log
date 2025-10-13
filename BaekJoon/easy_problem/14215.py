# 백준 14215 : 세 막대

triangle = list(map(int, input().split()))

while max(triangle) >= (sum(triangle)-max(triangle)):
    index = triangle.index(max(triangle))
    triangle[index] -= 1
    
print(sum(triangle))
