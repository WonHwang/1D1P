# 1D1P Day296 BOJ 9610번 사분면 문제 - 2021.08.27

N = int(input())
Q1, Q2, Q3, Q4, axis = 0, 0, 0, 0, 0

for _ in range(N):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        axis += 1
    
    elif x > 0 and y > 0:
        Q1 += 1
    
    elif x < 0 and y > 0:
        Q2 += 1
    
    elif x < 0 and y < 0:
        Q3 += 1
    
    else:
        Q4 += 1

print('Q1:', Q1)
print('Q2:', Q2)
print('Q3:', Q3)
print('Q4:', Q4)
print('AXIS:', axis)