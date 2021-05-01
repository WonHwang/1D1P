# 1D1P Day178 programmers 2019 카카오 개발자 겨울 인턴십 크레인 인형뽑기 문제 - 2021.05.01

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

def solution(board, moves):

    N = len(board)
    
    queues = [[] for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            if board[j][i]:
                queues[i+1].append(board[j][i])
    results = []
    answer = 0

    for num in moves:
        if queues[num]:
            results.append(queues[num].pop(0))

            if len(results) >= 2 and results[-1] == results[-2]:
                results.pop()
                results.pop()
                answer += 2
    
    return answer

print(solution(board, moves))