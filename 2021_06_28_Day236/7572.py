# 1D1P Day236 BOJ 7572번 간지 문제 - 2021.06.28

G = '6789012345'
J = 'IJKLABCDEFGH'

N = int(input())
answer = J[N%12] +  G[N%10]
print(answer)