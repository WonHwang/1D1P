# 1D1P Day192 BOJ 2587번 대표값2 문제 - 2021.05.15

numbers = []

for _ in range(5):
    numbers.append(int(input()))

numbers.sort()

print(sum(numbers) // 5)
print(numbers[2])