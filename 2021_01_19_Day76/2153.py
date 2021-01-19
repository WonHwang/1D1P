# 1D1P Day76 BOJ 2153번 소수 단어 문제 - 2021.01.19

word = input()

primes = [1] * 2000
primes[0] = 0
primes[1] = 1

for i in range(4, 2000):
    for j in range(2, int(i ** 0.5) + 1):
        if not (i % j):
            primes[i] = 0
            break

result = 0
for i in range(len(word)):
    if 'a' <= word[i] <= 'z':
        result += ord(word[i]) - ord('a') + 1
    else:
        result += ord(word[i]) - ord('A') + 27

if primes[result]:
    print("It is a prime word.")
else:
    print("It is not a prime word.")