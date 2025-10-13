# 백준 1316 : 그룹 단어 체커

import sys

# 단어의 개수 입력받기
n = int(input())

# n개의 단어 입력
word_li = []
for _ in range(n):
    word_li.append(sys.stdin.readline().strip())

# make def. to check this word is group word
def check_groupWord(word):
    check_set = set()
    alphabet = word[0]
    check_set.add(alphabet)

    for a in word:
        if a == alphabet:
            continue
        else:
            if a in check_set:
                return 0
            else:
                alphabet = a
                check_set.add(a)

    return 1

# Let's check using word_list!
output = 0
for word in word_li:
    output += check_groupWord(word)

print(output)