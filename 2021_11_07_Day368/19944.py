# 1D1P Day368 BOJ 19944번 뉴비의 기준은 뭘까? 문제 - 2021.11.07

N, M = map(int, input().split())

if 1 <= M <= 2:
    print('NEWBIE!')

elif 2 < M <= N:
    print('OLDBIE!')

else:
    print('TLE!')