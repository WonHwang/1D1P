# 1D1P Day79 SWEA 1945번 간단한 소인수분해 문제 - 2021.01.22

def soinsuboonhae(N):
    soinsu = [2, 3, 5, 7, 11]
    answer = [0] * 5

    for i in range(5):
        while N % soinsu[i] == 0:
            N //= soinsu[i]
            answer[i] += 1
    
    for i in range(5):
        print(answer[i], end = " ")
    print()

for _ in range(1, int(input())+1):
    N = int(input())
    print(f"#{_}", end = " ")
    soinsuboonhae(N)