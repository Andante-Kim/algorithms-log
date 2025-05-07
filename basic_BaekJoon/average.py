n = int(input())

score = []
score.extend(map(int, input().split()))

m = max(score)
sum_score = 0

for i in range(n):
  score[i] = score[i] / m * 100
  sum_score += score[i]

print(sum_score/n)