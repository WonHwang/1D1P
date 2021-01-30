# 1D1P Day87 BOJ 5397번 키로거 문제 - 2021.01.30

for _ in range(int(input())):
    string = input()
    stack1 = []
    stack2 = []

    for i in range(len(string)):
        if string[i] == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif string[i] == '>':
            if stack2:
                stack1.append(stack2.pop())
        elif string[i] == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(string[i])
    
    while stack2:
        stack1.append(stack2.pop())
    
    result = ''.join(stack1[:])

    print(result)