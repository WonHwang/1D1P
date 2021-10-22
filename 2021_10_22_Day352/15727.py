# 1D1P Day352 BOJ 15727번 조별과제를 하려는데 조장이 사라졌다 문제 - 2021.10.22

N = int(input())
answer = N // 5
if N%5:
    answer += 1
print(answer)