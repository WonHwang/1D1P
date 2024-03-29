# 1D1P Day291 BOJ 15892번 Hashing 문제 - 2021.08.22

r = 31
M = 1234567891

L = int(input())
string = input()

square = [1] * 50

for i in range(1, 50):
    square[i] = (square[i-1] * r) % M

answer = 0

for i in range(L):
    answer += ((ord(string[i]) - ord('a') + 1) * square[i]) % M

print(answer % M)