# 2941 : 크로아티아 알파벳

word = input()

cro_alphabet = ['c=','dz=', 's=' , 'z=',
               'c-', 'd-', 'lj', 'nj']

count = 0
t = len(word) - 1
while t > -1:
  if word[t] == '=':
    if word[t-2:t] == 'dz':
      t -= 3
      count += 1
    else:
      t -= 2
      count += 1
  elif word[t] == '-':
    t -= 2
    count += 1
  elif word[t] == 'j':
    if word[t-1] == 'l' or word[t-1] == 'n':
      t -= 2
      count += 1
    else:
      t -= 1
      count += 1
  else:
    t -= 1
    count += 1

print(count)