# 1D1P Day348 BOJ 14652번 나는 행복합니다~ 문제 - 2021.10.18

N, M, K = map(int, input().split())
n = K // M
m = K % M
print(n, m)


# 쓸데없이 메모리를 많이쓰면 메모리초과가 난다!

# N, M, K = map(int, input().split())

# grid = [[0 for _ in range(M)] for _ in range(N)]

# tmp = 0
# for i in range(N):
#     for j in range(M):
#         grid[i][j] = tmp
#         tmp += 1

# n, m = -1, -1
# for i in range(N):
#     for j in range(M):
#         if grid[i][j] == K:
#             n, m = i, j
#             break
#     if n != -1 and m != -1:
#         break

# print(n, m)