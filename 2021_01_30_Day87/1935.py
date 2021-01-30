# 1D1P Day87 BOJ 1935번 후위 표기식2 문제 - 2021.01.30

alphabet = {}
for i in range(ord('A'), ord('Z') + 1):
    alphabet[chr(i)] = 0

N = int(input())
string = input()
for i in range(N):
    alphabet[chr(ord('A')+i)] = float(input())

stack = []

for i in range(len(string)):
    if 'A' <= string[i] <= 'Z':
        stack.append(alphabet[string[i]])
    
    elif string[i] == '*':
        x = stack.pop()
        y = stack.pop()
        stack.append(x * y)
    
    elif string[i] == '/':
        x = stack.pop()
        y = stack.pop()
        stack.append(y / x)
    
    elif string[i] == '+':
        x = stack.pop()
        y = stack.pop()
        stack.append(x + y)
    
    elif string[i] == '-':
        x = stack.pop()
        y = stack.pop()
        stack.append(y - x)

print("%0.2f" % (stack.pop()))