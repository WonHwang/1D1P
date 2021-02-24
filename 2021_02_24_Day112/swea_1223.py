# 1D1P Day112 SWEA 1223번 계산기2 문제 - 2021.02.24

for tc in range(1, 11):
    N = int(input())
    inorder = input()
    postorder = []
    stack = []

    priority = {'+' : 1, '*' : 2}

    for char in inorder:

        if char == '+' or char == '*':
            while stack and priority[stack[-1]] >= priority[char]:
                postorder.append(stack.pop())
            stack.append(char)
        else:
            postorder.append(int(char))

    while stack:
        postorder.append(stack.pop())

    for char in postorder:
        if char == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        
        elif char == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        
        else:
            stack.append(char)

    answer = stack.pop()
    print(answer)