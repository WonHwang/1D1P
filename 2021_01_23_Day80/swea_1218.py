for t in range(1, 11):
    N = int(input())
    string = input()
    stack = []
    answer = 1
    for i in range(N):
        if string[i] == '(' or string[i] == '[' or string[i] == '{' or string[i] == '<':
            stack.append(string[i])
        elif string[i] == ')':
            if stack[-1] != '(':
                answer = 0
                break
            else:
                stack.pop()
        elif string[i] == ']':
            if stack[-1] != '[':
                answer = 0
                break
            else:
                stack.pop()
        elif string[i] == '}':
            if stack[-1] != '{':
                answer = 0
                break
            else:
                stack.pop()
        elif string[i] == '>':
            if stack[-1] != '<':
                answer = 0
                break
            else:
                stack.pop()
    print(f"#{t} {answer}")