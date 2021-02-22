# 1D1P Day110 SWEA 4866번 괄호 검사 문제 - 2021.02.22

for tc in range(1, int(input()) + 1):

    string = input()
    stack = []

    answer = 1
    for char in string:
        if char == '{' or char == '(':
            stack.append(char)
        
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                continue
            answer = 0
            break
        
        elif char == '}':
            if stack and stack[-1] == '{':
                stack.pop()
                continue
            answer = 0
            break

    if answer and stack:
        answer = 0
    
    print(f"#{tc} {answer}")