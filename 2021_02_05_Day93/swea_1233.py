# 1D1P Day SWEA 1233번 사칙연산 유효성 검사 문제 - 2021.02.05

for t in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    link = [[0, 0] for _ in range(N+1)]

    answer = 1

    for i in range(N):
        string = input().split()
        index = int(string[0])
        value = string[1]

        if len(string) == 2:
            if value == '+' or value == '-' or value == '*' or value == '/':
                answer = 0
        
        elif len(string) == 3:
            answer = 0
        
        elif len(string) == 4:
            if value != '+' and value != '-' and value != '*' and value != '/':
                answer = 0
    
    print(f"#{t} {answer}")