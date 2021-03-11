# 1D1P Day127 BOJ 10162번 전자레인지 문제 - 2021.03.11

T = int(input())

A, B, C = 0, 0, 0

answer = True

while T > 0:

    if T >= 300:
        A += 1
        T -= 300
    
    elif T >= 60:
        B += 1
        T -= 60
    
    elif T >= 10:
        C += 1
        T -= 10
    
    else:
        answer = False
        break

if answer:
    print(A, B, C)
else:
    print(-1)