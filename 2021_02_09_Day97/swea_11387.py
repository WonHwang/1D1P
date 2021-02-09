# 1D1P Day97 SWEA 11387번 몬스터 사냥 문제 - 2021.02.09

for tc in range(1, int(input())+1):
    D, L, N = map(int, input().split())
    answer = (D-L*(D//100))*N + ((N*(N+1))//2)*L*(D//100)
    print("#{} {}".format(tc, answer))