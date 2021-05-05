# 1D1P Day182 BOJ 1453번 피시방 알바 문제 - 2021.05.05

N = int(input())
numbers = list(map(int, input().split()))
visited = [0] * 101

answer = 0
for i in range(N):
    if not visited[numbers[i]]:
        visited[numbers[i]] = 1
    else:
        answer += 1

print(answer)