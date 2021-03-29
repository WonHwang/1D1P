from sys import stdin
input = stdin.readline

N, K, M = map(int, input().split())


if K%N:
    target = K%N
else:
    target = N

answer = 0
while True:
    answer += 1

    if target == M:
        break

    if M - target > 0:
        M -= target
        N -= 1

    else:
        M += N - target
        N -= 1
    
    if K%N:
        target = K%N
    else:
        target = N

print(answer)