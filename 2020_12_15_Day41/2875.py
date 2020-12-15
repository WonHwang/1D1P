# 1D1P Day41 BOJ 2875번 대회 or 인턴 문제 - 2020.12.15

N, M, K = map(int, input().split(' '))

answer = 0
for i in range(K+1):
    woman = N-i
    man = M-K+i

    woman_divided_2 = woman // 2

    if man > woman_divided_2:
        result = woman_divided_2
    else:
        result = man
    
    if result > answer:
        answer = result

print(answer)