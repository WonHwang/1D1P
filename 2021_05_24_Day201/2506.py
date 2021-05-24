# 1D1P Day201 BOJ 2506번 점수계산 문제 - 2021.05.24

N = int(input())
answers = list(map(int, input().split()))

tmp = 1
answer = 0
for i in range(N):
    if answers[i]:
        answer += tmp
        tmp += 1
    else:
        tmp = 1

print(answer)