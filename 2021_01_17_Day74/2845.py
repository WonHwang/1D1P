# 1D1P Day74 BOJ 2845번 파티가 끝나고 난 뒤 문제 - 2021.01.17

N, K = map(int, input().split(' '))
answer = list(map(int, input().split(' ')))
tmp = N * K
for i in range(5):
    answer[i] -= tmp
for i in range(5):
    print(answer[i], end=" ")