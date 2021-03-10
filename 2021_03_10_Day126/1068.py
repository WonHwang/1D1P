# 1D1P Day126 BOJ 1068번 트리 문제 - 2021.03.10

def dfs(x):

    global answer

    if not tree[x]:
        answer += 1
        return

    for v in tree[x]:
        dfs(v)

N = int(input())
info = list(map(int, input().split()))
tree = [[] for _ in range(N)]
delete = int(input())

for i in range(N):
    if info[i] == -1:
        root = i
        continue
    if i == delete:
        continue
    tree[info[i]].append(i)


answer = 0
if root != delete:
    dfs(root)
print(answer)