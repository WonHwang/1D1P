# 1D1P Day306 BOJ 2476번 주사위 게임 문제 - 2021.09.06

answer = 0

for _ in range(int(input())):

    a, b, c = map(int, input().split())

    if a == b == c:
        tmp = 10000 + 1000 * a
    
    elif a == b:
        tmp = 1000 + 100 * a
    
    elif b == c:
        tmp = 1000 + 100 * b
    
    elif c == a:
        tmp = 1000 + 100 * c
    
    else:
        tmp = max(a, b, c) * 100
    
    if tmp > answer:
        answer = tmp

print(answer)