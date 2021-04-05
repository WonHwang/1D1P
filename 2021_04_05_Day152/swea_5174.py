# 1D1P Day152 SWEA 파이썬 SW문제해결 기본 Tree 5174번 subtree 문제 - 2021.04.05

answer = 0

def count(tree, N):

    global answer

    answer += 1

    if not tree[N]:
        return
    
    for child in tree[N]:
        count(tree, child)

for tc in range(1, int(input()) + 1):

    E, N = map(int, input().split())

    info = list(map(int, input().split()))

    tree = [[] for _ in range(E+2)]

    for i in range(E):
        tree[info[2*i]].append(info[2*i + 1])
    
    answer = 0

    count(tree, N)

    print(f"#{tc} {answer}")