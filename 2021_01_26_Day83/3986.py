# 1D1P Day83 BOJ 3986번 좋은 단어 문제 - 2021.01.26

answer = 0
for _ in range(int(input())):
    word = input()
    stack = []
    for i in word:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if not stack:
        answer += 1
print(answer)