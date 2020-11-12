# 1D1P Day8 BOJ 6588번 골드바흐의 추측 문제 - 2020.11.12

import sys

erathostenes_sieve = [0] * 1000001

for i in range(2, 1000001):
    if i%2 == 0:
        continue
    erathostenes_sieve[i] = i

erathostenes_sieve[2] = 2

for i in range(3, 1000001, 2):
    if erathostenes_sieve[i] != 0:
        for j in range(3, int(i**0.5) + 1, 2):
            if i % j == 0:
                for k in range(1, int(1000001/i)+1, 2):
                    erathostenes_sieve[i*k] = 0
                break

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    answer = ""
    for i in range(3, N, 2):
        if erathostenes_sieve[i] != 0 and erathostenes_sieve[N-i]!=0:
            answer = str(N) + " = " + str(i) + " + " + str(N-i)
            break
    if answer != "":
        print(answer)
    else:
        print("Goldbach's conjecture is wrong.")