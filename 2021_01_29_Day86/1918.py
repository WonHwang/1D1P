# 1D1P Day86 BOJ 1918번 후기 표기식 문제 - 2021.01.29

string = input()
stack = []
result = ""

for i in range(len(string)):

    if string[i] >= 'A' and string[i] <= 'Z':
        result += string[i]
    
    elif string[i] == '(':
        stack.append(string[i])
    
    elif string[i] == ')':
        while stack:
            if stack[-1] == '(':
                stack.pop()
                break
            result += stack.pop()
    
    elif string[i] == '*' or string[i] == '/':
        while stack:
            if stack[-1] == '(' or stack[-1] == '+' or stack[-1] == '-':
                break
            if stack[-1] == '*' or stack[-1] == '/':
                result += stack.pop()
        stack.append(string[i])
    
    elif string[i] == '+' or string[i] == '-':
        while stack:
            if stack[-1] == '(':
                break
            result += stack.pop()
        stack.append(string[i])

while stack:
    result += stack.pop()

print(result)