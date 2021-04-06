# 1D1P Day153 BOJ 1323번 숫자 연결하기 문제 - 2021.04.06

N, K = map(int, input().split())
length = len(str(N))

N %= K

now = N
to_next = 10 ** length

answer = 1

visited = [0] * K

while True:
    if now == 0:
        break
    visited[now] = 1

    now = ((now * to_next) + N) % K
    if visited[now]:
        answer = -1
        break
    answer += 1

print(answer)