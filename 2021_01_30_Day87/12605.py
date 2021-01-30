# 1D1P Day87 BOJ 12605번 단어순서 뒤집기 문제 - 2021.01.30

N = int(input())

for i in range(1, N+1):
    stack = input().split()

    print(f"Case #{i}: ", end = '')

    while stack:
        print(stack.pop(), end = ' ')
    print()