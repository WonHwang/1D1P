# 1D1P Day79 SWEA 1983번 조교의 성적 매기기 문제 - 2021.01.22

for _ in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    score = []
    for i in range(N):
        mid, final, hw = map(int, input().split())
        score.append(mid*0.35 + final*0.45 + hw*0.2)
    K_score = score[K-1]
    score.sort()
    K_rank = score.index(K_score) + 1
    for i in range(10):
        if i * (N // 10) < K_rank <= (i + 1) * (N // 10):
            K_degree = i + 1
    if K_degree < 2:
        answer = "D0"
    elif K_degree < 3:
        answer = "C-"
    elif K_degree < 4:
        answer = "C0"
    elif K_degree < 5:
        answer = "C+"
    elif K_degree < 6:
        answer = "B-"
    elif K_degree < 7:
        answer = "B0"
    elif K_degree < 8:
        answer = "B+"
    elif K_degree < 9:
        answer = "A-"
    elif K_degree < 10:
        answer = "A0"
    else:
        answer = "A+"
    
    print(f"#{_} {answer}")