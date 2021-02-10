# 1D1P Day98 SWEA 4837번 부분집합의 합 문제 - 2021.02.10

A = [i for i in range(1,13)]
answer = 0
def subset(N, K, count, element, visited):

    global answer

    if count == N:
        if sum(element) == K:
            answer += 1
        return
    
    if not element:
        for i in range(1, 13-N):
            element.append(i)
            visited[i] = 1
            subset(N, K, count+1, element, visited)
            visited[element.pop()] = 0
    else:
        for i in range(element[-1], 13):
            if visited[i] == 0:
                element.append(i)
                visited[i] = 1
                subset(N, K, count+1, element, visited)
                visited[element.pop()] = 0
            

for tc in range(1, int(input()) + 1):
    
    N, K = map(int, input().split())
    answer = 0
    visited = [0] * 13
    subset(N, K, 0, [], visited)

    print(f"#{tc} {answer}")