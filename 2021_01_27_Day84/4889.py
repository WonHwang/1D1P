from sys import stdin

test = 0
while True:
    test += 1
    stack = []
    string = stdin.readline().rstrip()
    if string[0] == '-':
        break
    for i in range(len(string)):
        if stack:
            if stack[-1] == '{' and string[i] == '}':
                stack.pop()
                continue
        stack.append(string[i])
    answer = 0
    while stack:
        if stack[-1] == '{':
            if stack[-2] == '{':
                stack.pop()
                stack.pop()
                answer += 1
            else:
                stack.pop()
                stack.pop()
                answer += 2
        else:
            stack.pop()
            stack.pop()
            answer += 1
    
    print(f"{test}. {answer}")