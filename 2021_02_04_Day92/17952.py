# 1D1P Day92 BOJ 17952번 과제는 끝나지 않아! 문제 - 2021.02.04

from sys import stdin

N = int(stdin.readline().rstrip())

stack = []
answer = 0
for _ in range(N):
    tmp = stdin.readline().rstrip()
    if tmp == '0':
        if stack:
            hw = stack.pop()
            score, time = hw[0], hw[1]
            if time == 1:
                answer += score
            else:
                stack.append([score, time - 1])
    else:
        tmp = tmp.split()
        score, time = int(tmp[1]), int(tmp[2])
        if time == 1:
            answer += score
        else:
            stack.append([score, time - 1])

print(answer)