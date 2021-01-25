string = input()
key = list(input())
key_length = len(key)
stack = []

def bomb():
    while len(stack) >= key_length:
            if stack[-key_length:] == key:
                for _ in range(key_length):
                    stack.pop()
            else:
                break

for i in range(len(string)):
    stack.append(string[i])
    if len(stack) >= key_length:
        bomb()

if stack:
    answer = ""
    for _ in stack:
        answer += _
    print(answer)
else:
    print("FRULA")