# 1D1P Day78 SWEA 1284번 수도 요금 경쟁 문제 - 2021.01.21

T = int(input())
for _ in range(T):
    P, Q, R, S, W = map(int, input().split(' '))
    A = P * W
    if W > R:
        B = Q + (W-R) * S
    else:
        B = Q
    
    print(f"#{_+1}", end=" ")
    print(A if A <= B else B)