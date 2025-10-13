# 백준 2720 : 세탁소 사장 동혁

# T : the number of test cases
T = int(input())

test_case = []
money = [[0]*4 for _ in range(T)]

for _ in range(T):
    change = int(input())
    test_case.append(change)

for i in range(len(test_case)):
    # Quarter, $0.25
    money[i][0] = test_case[i] // 25
    test_case[i] -= money[i][0]*25
    # Dime, $0.10
    money[i][1] = test_case[i] // 10
    test_case[i] -= money[i][1]*10
    # Nickel, $0.05
    money[i][2] = test_case[i] // 5
    test_case[i] -= money[i][2]*5
    # Penny, $0.01
    money[i][3] = test_case[i] // 1
    test_case[i] -= money[i][3]*1
    
for n in money:
    for m in n:
        print(m,end=' ')
    print()
