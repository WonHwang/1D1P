# 1D1P Day110 SWEA 4873번 반복 문자 지우기 문제 - 2021.02.22

for tc in range(1, int(input()) + 1):
    string = input()
    stack = []
    for char in string:
        stack.append(char)

        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    print(f"#{tc} {len(stack)}")