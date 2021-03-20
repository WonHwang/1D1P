N = int(input())

maps = list(map(int, list(input())))
DP = [0] * N

DP[0] = 1
for i in range(N):
    if maps[i] == 1:
        if i+2 < N and maps[i+2] == 1:
            DP[i+2] += DP[i]
        
        if i+1 < N and maps[i+1] == 1:
            DP[i+1] += DP[i]

print(DP[N-1])