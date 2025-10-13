# 백준 10798 : 세로 읽기

# input 5 lines
li = []
max_len = 0

for _ in range(5):
  word = ' '.join(str(input()))
  word = list(map(str, word.split()))
  li.append(word)
  if len(word) > max_len:
    max_len = len(word)

# print result
for j in range(max_len):
  for i in range(5):
    try:
      result = li[i][j]
      print(result,end='')
    except:
      continue
