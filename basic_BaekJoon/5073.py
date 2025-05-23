# 백준 5073 : 삼각형과 세 변

import sys

triangles = list(map(int, sys.stdin.readline().split()))
while triangles != [0, 0, 0]:
    # 삼각형 조건 검사
    if max(triangles) >= (sum(triangles) - max(triangles)):
        print('Invalid')
    # 두 변의 길이가 같을 때 vs 모두 다를 때 분류하기
    elif triangles[0] == triangles[1]:
        if triangles[0] == triangles[2]:     # 세 변이 모두 같다면
            print('Equilateral')
        else:
            print('Isosceles')   # 두 변만 같을 때때
    elif triangles[1] == triangles[2]:
        if triangles[1] == triangles[0]:
            print('Equilateral')
        else:
            print('Isosceles')
    elif triangles[2] == triangles[0]:
        if triangles[2] == triangles[1]:
            print('Equilateral')
        else:
            print('Isosceles')
    else:
        print('Scalene')
    triangles = list(map(int, sys.stdin.readline().split()))
