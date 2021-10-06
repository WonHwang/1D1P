# 1D1P Day336 BOJ 13699번 점화식 문제 - 2021.10.06

T = [0] * 36
T[0] = 1

for i in range(1, 36):
    for j in range(i):
        T[i] += T[j] * T[i-j-1]

print(T[int(input())])