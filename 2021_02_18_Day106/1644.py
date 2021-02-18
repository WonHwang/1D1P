# 1D1P Day106 BOJ 1644번 소수의 연속합 문제 - 2021.02.18

sieve = [1] * 4000001

for i in range(4, 4000001, 2):
    sieve[i] = 0

sieve[0] = 0
sieve[1] = 0

for i in range(3, 4000001, 2):
    if sieve[i] == 1:
        for j in range(2*i, 4000001, i):
            sieve[j] = 0

numbers = []
for i in range(4000001):
    if sieve[i] == 1:
        numbers.append(i)

N = int(input())

length = len(numbers)
start = 0
end = 0
total = numbers[0]
answer = 0
while True:

    if start > end or numbers[start] > N:
        break

    if total == N:
        answer += 1
        end += 1
        if end == length:
            break
        total += (numbers[end] - numbers[start])
        start += 1
    
    if total > N:
        total -= numbers[start]
        start += 1
    
    if total < N:
        end += 1
        if end == length:
            break
        total += numbers[end]

print(answer)