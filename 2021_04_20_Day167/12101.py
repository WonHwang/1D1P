# 1D1P Day167 BOJ 12101번 1,2,3 더하기 2 문제 - 2021.04.20

cnt = 0
flag = 1

def dfs(element, N, K):

    global cnt

    if sum(element) == N:
        cnt += 1
        if cnt == K:
            global flag
            answer = ''
            for num in element:
                answer += str(num)
                answer += '+'
            print(answer[:-1])
            flag = 0
        return
    
    if sum(element) > N:
        return
    
    for i in range(1, 4):
        element.append(i)
        dfs(element, N, K)
        element.pop()

N, K = map(int, input().split())

dfs([], N, K)

if flag:
    print(-1)