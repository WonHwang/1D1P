# 1D1P Day152 SWEA 1231번 중위순회 문제 - 2021.04.05

answer = ''

def inorder(tree, node):

    global answer

    if tree[node][0]:
        inorder(tree, tree[node][0])
    
    answer += tree_value[node]

    if tree[node][1]:
        inorder(tree, tree[node][1])

for tc in range(1, 11):

    N = int(input())

    tree = [[0, 0] for _ in range(N+1)] # [left, right]
    tree_value = [''] * (N+1) # value만 따로 처리 - 값이 str이라서..

    for _ in range(N):
        tmp = list(input().split())

        K = int(tmp[0])

        if len(tmp) > 3:
            tree_value[K] = tmp[1]
            tree[K][0] = int(tmp[2])
            tree[K][1] = int(tmp[3])
        
        elif len(tmp) > 2:
            tree_value[K] = tmp[1]
            tree[K][0] = int(tmp[2])
        
        else:
            tree_value[K] = tmp[1]
    
    answer = ''

    inorder(tree, 1)

    print(f"#{tc} {answer}")