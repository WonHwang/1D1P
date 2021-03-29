# 1D1P Day145 BOJ 12907번 동물원 문제 - 2021.03.29

N = int(input())
answers = list(map(int, input().split()))
Max = max(answers)
cnt = [0] * N
answer = 1
for ans in answers:
    if ans < N:
        cnt[ans] += 1
    
    else:
        answer = 0
        break

if answer:
    for i in range(N):
        if cnt[i] > 2:
            answer = 0
            break
        elif cnt[i] == 1:
            for j in range(i, N):
                if cnt[j] > 1:
                    answer = 0
                    break
        elif cnt[i] == 0:
            for j in range(i, N):
                if cnt[j] > 0:
                    answer = 0
                    break
        
        if not answer:
            break

if answer:
    for i in range(N):
        if cnt[i] == 2:
            answer *= 2
    
    if cnt[Max] == 1:
        answer *= 2

print(answer)