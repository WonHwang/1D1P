# 1D1P Day297 BOJ 2720번 세탁소 사장 동혁 문제 - 2021.08.28

for _ in range(int(input())):

    change = int(input())
    Q, D, N, P = 0, 0, 0, 0
    while change > 0:

        if change >= 25:
            change -= 25
            Q += 1
          
        elif change >= 10:
            change -= 10
            D += 1
        
        elif change >= 5:
            change -= 5
            N += 1
        
        else:
            change -= 1
            P += 1
    
    print(Q, D, N, P)