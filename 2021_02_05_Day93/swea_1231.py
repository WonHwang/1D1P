# 1D1P Day93 SWEA 1231번 중위 순회 문제 - 2021.02.05

for t in range (1, 11):
    N = int(input())
    tree = [[0, 0] for _ in range(N+1)]
    alpha = [0] * (N+1)

    for i in range(N):
        string = input().split()
        alpha[int(string[0])] = string[1]
        
        if len(string) == 4:
            tree[int(string[0])][0] = int(string[2])
            tree[int(string[0])][1] = int(string[3])
        
        elif len(string) == 3:
            tree[int(string[0])][0] = int(string[2])
    
    
    answer = ""

    def midorder(i):
        global answer

        if tree[i][0]:
            midorder(tree[i][0])
        
        answer += alpha[i]

        if tree[i][1]:
            midorder(tree[i][1])
    
    midorder(1)

    print(f"#{t} {answer}")