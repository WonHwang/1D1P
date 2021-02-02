# 1D1P Day90 BOJ 16120번 PPAP 문제 - 2021.02.02

string = input()

stack = []

for i in range(len(string)):
    stack.append(string[i])
    if len(stack) >= 4:
        if ''.join(stack[-4:]) == 'PPAP':
            stack.pop()
            stack.pop()
            stack.pop()
            continue

if stack and len(stack) == 1 and stack.pop() == 'P':
    print("PPAP")
else:
    print("NP")