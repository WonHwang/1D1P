# 1D1P Day152 BOJ 9934번 완전 이진 트리 문제 - 2021.04.05

K = int(input())
inorder = list(map(int, input().split()))

level = [[] for _ in range(K)]

def makelevel(inorder, depth):

    global level

    if not inorder:
        return

    mid = len(inorder) // 2
    level[depth].append(inorder[mid])

    makelevel(inorder[:mid], depth+1)
    makelevel(inorder[mid+1:], depth+1)

makelevel(inorder, 0)

for i in range(K):
    print(*level[i])