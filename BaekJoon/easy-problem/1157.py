# 백준 1157 : 단어 공부

word = input()

alphabet_count = [0] * 26

# change upper to lower
for k in word:
  # ord('A') = 65, ord('a')=97
  if ord(k) >= 97:
    k = chr(ord(k) - 32)
  # add alphabet in list
  alphabet_count[ord(k)-65] += 1

#print(alphabet_count)

max_index = [0,]
for t in range(1, 26):
  num = alphabet_count[max_index[0]]
  if alphabet_count[t] > num:
    max_index = []
    max_index.append(t)
  elif alphabet_count[t] == num:
    max_index.append(t)

#print(max_index)
if len(max_index) > 1:
  print("?")
else:
  print(chr(max_index[0] + 65))