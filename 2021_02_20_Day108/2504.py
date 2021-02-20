# 1D1P Day108 BOJ 2504번 괄호의 값 문제 - 2021.02.20

string = input()

stack = []

for char in string:
    if char == ')' and stack:
        if stack[-1] == '(':
            stack.pop()
    elif char == ']' and stack:
        if stack[-1] == '[':
            stack.pop()
    else:
        stack.append(char)

if stack:
    is_valid = 0
else:
    is_valid = 1

answer = 0
if is_valid:
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        
        elif char == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
                continue
            
            tmp = 0
            while type(stack[-1]) is int:
                tmp += stack.pop()
            
            if stack[-1] == '(':
                stack.pop()
                stack.append(2 * tmp)
        
        elif char == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
                continue

            tmp = 0
            while type(stack[-1]) is int:
                tmp += stack.pop()
            
            if stack[-1] == '[':
                stack.pop()
                stack.append(3 * tmp)
    
    while stack:
        answer += stack.pop()

print(answer)