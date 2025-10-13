
n = int(input())

word_li = [input() for _ in range(n)]

for word in word_li:
    alpha_li = []
    for k in range(len(word)):
        if (word[k] in alpha_li) and (word[k] != word[k-1]):
            n -= 1
            break
        else:
            alpha_li.append(word[k])

print(n)