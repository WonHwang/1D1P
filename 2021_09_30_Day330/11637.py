# 1D1P Day330 BOJ 11637번 인기 투표 문제 - 2021.09.30

for _ in range(int(input())):

    candidate = []
    N = int(input())
    for _ in range(N):
        candidate.append(int(input()))
    
    cnt = 0
    answer = 0
    Max = max(candidate)
    for i in range(len(candidate)):
        if Max == candidate[i]:
            cnt += 1
            answer = i+1
        
        if cnt >= 2:
            answer = 0
            break
    
    if answer:
        if Max > sum(candidate) // 2:
            print(f'majority winner {answer}')
        else:
            print(f'minority winner {answer}')
    
    else:
        print('no winner')