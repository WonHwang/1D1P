# 1D1P Day79 SWEA 1970번 쉬운 거스름돈 문제 - 2021.01.22

def change(N):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = [0] * 8

    for i in range(8):
        while N >= money[i]:
            N -= money[i]
            answer[i] += 1
    
    for i in range(8):
        print(answer[i], end = " ")
    print()

for _ in range(1, int(input())+1):
    N = int(input())
    print(f"#{_}")
    change(N)