# 1D1P Day254 BOJ 1267번 핸드폰 요금 문제 - 2021.07.16

N = int(input())
times = list(map(int, input().split()))

Y, M = 0, 0
for time in times:
    for i in range((time//30) + 2):
        if 30*i <= time < 30*(i+1):
            Y += 10*(i+1)

    for i in range((time//60) + 2):
        if 60*i <= time < 60*(i+1):
            M += 15*(i+1)

if Y > M:
    print(f'M {M}')
elif Y < M:
    print(f'Y {Y}')
else:
    print(f'Y M {Y}')
