# 1D1P Day90 SWEA 1234번 비밀번호 문제 - 2021.02.02

for t in range(1, 11):
    N, numbers = input().split()
    stack = []
    stack.append(numbers[0])
    for i in range(1, int(N)):
        if stack and numbers[i] == stack[-1]:
            stack.pop()
            continue
        stack.append(numbers[i])
    answer = ''.join(stack)
    print(f"#{t} {answer}")