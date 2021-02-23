# 1D1P Day111 Programmers DFS/BFS 4번 여행경로 문제 - 2021.02.23

def solution(tickets):

    answer = []
    target = [1] * len(tickets)
    def dfs(n):

        visited[n] = 1

        if len(element) == len(tickets):
            if visited == target:
                tmp = []
                tmp.append(tickets[element[0]][0])
                for ele in element:
                    tmp.append(tickets[ele][1])
                answer.append(tmp)                
            return
        
        

        for i in range(len(tickets)):
            if tickets[n][1] == tickets[i][0] and visited[i] == 0:
                element.append(i)
                dfs(i)
                visited[element.pop()] = 0
    
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visited = [0] * len(tickets)
            element = []
            element.append(i)
            dfs(i)
            element.pop()
    
    answer.sort()
    return answer[0]
    
print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))