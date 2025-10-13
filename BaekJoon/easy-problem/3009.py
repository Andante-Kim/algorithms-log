# 백준 3009 : 네 번째 점

dot1 = list(map(int, input().split()))
dot2 = list(map(int, input().split()))
dot3 = list(map(int, input().split()))

dot4 = [0,0]

# find x of dot4
if dot1[0] == dot2[0]:
    dot4[0] = dot3[0]
    if dot3[1] == dot1[1]:
        dot4[1] = dot2[1]
    elif dot3[1] == dot2[1]:
        dot4[1] = dot1[1]

elif dot2[0] == dot3[0]:
    dot4[0] = dot1[0]
    if dot1[1] == dot2[1]:
        dot4[1] = dot3[1]
    elif dot1[1] == dot3[1]:
        dot4[1] = dot2[1]

elif dot1[0] == dot3[0]:
    dot4[0] = dot2[0]
    if dot2[1] == dot1[1]:
        dot4[1] = dot3[1]
    elif dot2[1] == dot3[1]:
        dot4[1] = dot1[1]

print(dot4[0], dot4[1])
