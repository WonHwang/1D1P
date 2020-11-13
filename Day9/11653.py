# 1D1P Day9 BOJ 11653번 소인수분해 문제 - 2020.11.13

eratosthenes = [0] * 3200

for i in range(3200):
    if i%2 == 1:
        eratosthenes[i] = i

eratosthenes[2] = 2

for i in range(3, 3200, 2):
    if eratosthenes[i] != 0:
        for j in range(3, int(i**0.5) + 1, 2):
            if i%j == 0:
                eratosthenes[i] = 0
                break


N = int(input())

while True:
    for i in range(2, 3200):
        if eratosthenes[i] != 0 and N%i == 0:
            N = int(N/i)
            print(i)
            break
    if N == 1:
        break
    if N > 3199 and i == 3199:
        print(N)
        break
