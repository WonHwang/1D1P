# 1D1P Day72 BOJ 1057번 토너먼트 문제 - 2021.01.15

N, A, B = map(int, input().split(' '))

if A > B:
    A, B = B, A

step = 1

while N >= 2:
    
    
    if A % 2 == 1 and B == A + 1:
        break

    if A % 2 == 0:
        A //= 2
    else:
        A = (A // 2) + 1
    
    if B % 2 == 0:
        B //= 2
    else:
        B = (B // 2) + 1
    
    if N % 2 == 0:
        N //= 2
    else:
        N = (N // 2) + 1
    
    step += 1

print(step)