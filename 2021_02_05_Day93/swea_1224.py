# 1D1P Day93 SWEA 1224번 계산기 3 문제 - 2021.02.05

for t in range(1, 11):
    N = int(input())
    string = input()
    stack = []
    postorder = ""
    for i in range(N):
        if string[i] == '+':
            while stack and stack[-1] != '(':
                postorder += stack.pop()
            stack.append(string[i])
        
        elif string[i] == '*':
            while stack and stack[-1] == '*':
                postorder += stack.pop()
            stack.append(string[i])
        
        elif string[i] == '(':
            stack.append(string[i])
        
        elif string[i] == ')':
            while stack[-1] != '(':
                postorder += stack.pop()
            stack.pop()
        
        else:
            postorder += string[i]

    while stack:
        postorder += stack.pop()

    for i in range(len(postorder)):
        if postorder[i] == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(str(a+b))
        
        elif postorder[i] == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(str(a*b))
        
        else:
            stack.append(postorder[i])
    
    print(f"#{t} {stack.pop()}")