# 1D1P Day154 BOJ 10867번 중복 빼고 정렬하기 문제 - 2021.04.07

N = int(input())
numbers = list(map(int, input().split()))
numbers = list(set(numbers))
numbers.sort()
print(*numbers)