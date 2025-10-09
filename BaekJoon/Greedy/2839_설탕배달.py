# 백준 2839: 설탕 배달

n = int(input())

bag_5 = n//5
output = -1

#print(bag_5)
for i in range(bag_5, -1, -1):
    rest = n - (5*i)
    if rest%3 == 0:
        output = i + (rest//3)
        break

print(output)   
