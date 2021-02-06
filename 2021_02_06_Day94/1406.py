# 1D1P Day94 BOJ 1406번 에디터 문제 - 2021.02.06

from sys import stdin

string = stdin.readline().rstrip()
N = int(stdin.readline())
stack1 = list(string)
stack2 = []

for i in range(N):
    tmp = stdin.readline().rstrip()

    if tmp[0] == 'L' and stack1:
        stack2.append(stack1.pop())
        
    elif tmp[0] == 'D' and stack2:
        stack1.append(stack2.pop())
    
    elif tmp[0] == 'B' and stack1:
        stack1.pop()
    
    elif tmp[0] == 'P':
        stack1.append(tmp[2])
    
answer = ''.join(stack1 + stack2[::-1])

print(answer)