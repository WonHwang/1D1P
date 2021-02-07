# 1D1P Day95 BOJ 1009번 분산처리 문제 - 2021.02.07

def square(a, b):
    b = bin(b)
    b = b[2:]


    a_square = a
    answer = 1
    for i in range(len(b)-1, -1, -1):
        if b[i] == '1':
            answer *= a_square
        a_square *= a_square
        answer %= 10
        a_square %= 10
    
    return answer

for t in range(int(input())):
    a, b = map(int, input().split())

    answer = square(a, b)

    if answer:
        print(answer)
    else:
        print(10)