# 1D1P Day102 BOJ 1946번 신입 사원 문제 - 2021.02.14

from sys import stdin

for _ in range(int(stdin.readline())):

    N = int(stdin.readline())

    scores = []

    for i in range(N):
        scores.append(list(map(int, stdin.readline().rstrip().split())))
    
    scores.sort(key = lambda x : x[0])

    maxi = scores[0][1]
    answer = 1
    for i in range(1, N):
        if scores[i][1] < maxi:
            answer += 1
            maxi = scores[i][1]
    
    print(answer)