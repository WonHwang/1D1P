# 1D1P Day79 SWEA 1961번 숫자 배열 회전 문제 - 2021.01.22

for _ in range(1, int(input()) + 1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(input().split())
    
    def rotation(matrix, N):
        result = [['0' for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                result[i][j] = matrix[N-j-1][i]
        
        return result
    
    rotate_90 = rotation(matrix, N)
    rotate_180 = rotation(rotate_90, N)
    rotate_270 = rotation(rotate_180, N)

    for i in range(N):
        answer_90 = ""
        answer_180 = ""
        answer_270 = ""
        for j in range(N):
            answer_90 += rotate_90[i][j]
            answer_180 += rotate_180[i][j]
            answer_270 += rotate_270[i][j]
        print(f"{answer_90} {answer_180} {answer_270}")