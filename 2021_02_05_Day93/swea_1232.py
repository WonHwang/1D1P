# 1D1P Day93 SWEA 1232번 사칙연산 문제 - 2021.02.05

for t in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    link = [[-1, -1] for _ in range(N+1)]

    for i in range(N):
        string = input().split()
        index = int(string[0])
        node = string[1]

        if len(string) == 4:
            tree[index] = node
            link[index][0] = int(string[2])
            link[index][1] = int(string[3])
        
        else:
            tree[index] = int(node)
    

    def cal(tree, i):

        if type(tree[i]) == str:

            if type(tree[link[i][0]]) == str:
                cal(tree, link[i][0])

            if type(tree[link[i][1]]) == str:
                cal(tree, link[i][1])
            
            a = tree[link[i][0]]
            b = tree[link[i][1]]

            if tree[i] == '+':
                tree[i] = a + b
            
            elif tree[i] == '-':
                tree[i] = a - b
            
            elif tree[i] == '*':
                tree[i] = a * b
            
            else:
                tree[i] = a / b
    
    cal(tree, 1)
    print(f"#{t} {int(tree[1])}")