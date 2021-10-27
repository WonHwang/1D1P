# 1D1P Day357 BOJ 1173번 운동 문제 - 2021.10.27

N, m, M, T, R = map(int, input().split())
answer = 0
X = m

if m + T > M:
    answer = -1

else:
    cnt = 0
    while cnt < N:

        if X + T <= M:
            cnt += 1
            answer += 1
            X += T
        
        else:
            answer += 1
            X -= R

            if X < m:
                X = m

print(answer)