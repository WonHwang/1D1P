# 1D1P Day171 SWEA 7465번 창용 마을 무리의 개수 문제 - 2021.04.24

def make_set(N):
    return [i for i in range(N+1)]

def find_set(idx):

    while group[idx] != idx:
        idx = group[idx]
    
    return idx

def union(a, b):
    group[find_set(b)] = find_set(a)


for tc in range(1, int(input())+1):

    N, M = map(int, input().split())

    group = make_set(N)

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    
    answer = set()
    for i in range(1, N+1):
        answer.add(find_set(i))

    print(f"#{tc} {len(answer)}")