# 백준 25206 : 너의 평점은

import sys

# find score of grade
dic_grade = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

sum_credit = 0
sum_subject = 0

for _ in range(20):
    subject, credit, grade = map(str, input().split())
    # modify
    if grade == 'P':
        continue
    credit = float(credit)
    grade = dic_grade[grade]
    # input modifying value to score_list
    sum_credit += credit
    sum_subject += credit * grade

# Let's get answer
output = sum_subject / sum_credit
print('{:.6f}'.format(output))
