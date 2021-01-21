# 1D1P Day78 SWEA 11285번 다트 문제 - 2021.01.21
# sys 못쓰게 하면서 시간초과남... 걍 못푸는 문제

T = int(input())

for _ in range(1, T+1):
    N = int(input())
    answer = 0
    for __ in range(N):
        x, y = map(int, input().split(' '))
        score = (x ** 2) + (y ** 2)
        if score <= 400:
            answer += 10
        elif score <= 1600:
            answer += 9
        elif score <= 3600:
            answer += 8
        elif score <= 6400:
            answer += 7
        elif score <= 10000:
            answer += 6
        elif score <= 14400:
            answer += 5
        elif score <= 19600:
            answer += 4
        elif score <= 25600:
            answer += 3
        elif score <= 32400:
            answer += 2
        elif score <= 40000:
            answer += 1
    print(f"#{_} {answer}")