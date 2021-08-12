# 1D1P Day281 BOJ 1075번 나누기 문제 - 2021.08.12

N = input()
F = int(input())

digit = 0

while True:
    N = N[:-2] + str(digit).zfill(2)

    if not int(N) % F:
        break
    
    digit += 1

print(str(digit).zfill(2))