# 백준: 5622 다이얼

word = str(input())
dial = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
time = 0


for a in word:
  num = dial[ord(a)-65]
  time += (num + 1)

print(time)