string = input()
key = input()
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
    if len(stack) >= key_length - 1:
        if stack[-key_length + 1:] + string[i] == key:
            for _ in range(key_length):
                stack.pop()
            bomb()
        else:
            stack.append(string[i])
