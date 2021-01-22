# 1D1P Day79 SWEA 1288번 새로운 불면증 치료법 문제 - 2021.01.22

for _ in range(1, int(input()) + 1):
    N = int(input())
    visited = [0] * 10

    def all_visit():
        for i in range(10):
            if visited[i] == 0:
                return False
        return True
    
    def seedigit(N):
        while N != 0:
            visited[N % 10] = 1
            N //= 10
    tmp = N
    day = 0
    while not all_visit():
        seedigit(tmp)
        tmp += N
        day += 1
    print(f"#{_} {day * N}")
