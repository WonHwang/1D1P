// 1D1P Day85 BOJ 1987번 알파벳 문제 - 2021.01.28
// 아래 파이썬 코드로 작성했으나, 시간초과의 문제발생. 아무래도 dfs에는 안좋은 언어인듯..
// 완전 같은 논리로 작성했음

// R, C = map(int, input().split())
// board = []
// for _ in range(R):
//     board.append(input())

// answer = 0

// def dfs(x, y, visited, step):

//     global answer

//     if answer < step:
//         answer = step

//     if x > 0:
//         if visited[board[x-1][y]] == 0:
//             visited[board[x-1][y]] = 1
//             dfs(x-1, y, visited, step + 1)
//             visited[board[x-1][y]] = 0
    
//     if y > 0:
//         if visited[board[x][y-1]] == 0:
//             visited[board[x][y-1]] = 1
//             dfs(x, y-1, visited, step + 1)
//             visited[board[x][y-1]] = 0
    
//     if x < R-1:
//         if visited[board[x+1][y]] == 0:
//             visited[board[x+1][y]] = 1
//             dfs(x+1, y, visited, step + 1)
//             visited[board[x+1][y]] = 0
    
//     if y < C-1:
//         if visited[board[x][y+1]] == 0:
//             visited[board[x][y+1]] = 1
//             dfs(x, y+1, visited, step + 1)
//             visited[board[x][y+1]] = 0

// visited = {}
// for i in range(ord('A'), ord('Z') + 1):
//     visited[chr(i)] = 0
// visited[board[0][0]] = 1
// dfs(0, 0, visited, 1)

// print(answer)


#include <stdio.h>
#include <string.h>

int answer, R, C;
char board[21][21];

void dfs(int x, int y, int* visited, int step){
    
    if (answer < step) answer = step;
    
    if (x > 0){
        if (visited[board[x-1][y] - 'A'] == 0){
            visited[board[x-1][y] - 'A'] = 1;
            dfs(x-1, y, visited, step + 1);
            visited[board[x-1][y] - 'A'] = 0;
        }
    }
    if (y > 0){
        if (visited[board[x][y-1] - 'A'] == 0){
            visited[board[x][y-1] - 'A'] = 1;
            dfs(x, y-1, visited, step + 1);
            visited[board[x][y-1] - 'A'] = 0;
        }
    }
    if (x < R-1){
        if (visited[board[x+1][y] - 'A'] == 0){
            visited[board[x+1][y] - 'A'] = 1;
            dfs(x+1, y, visited, step + 1);
            visited[board[x+1][y] - 'A'] = 0;
        }
    }
    if (y < C-1){
        if (visited[board[x][y+1] - 'A'] == 0){
            visited[board[x][y+1] - 'A'] = 1;
            dfs(x, y+1, visited, step + 1);
            visited[board[x][y+1] - 'A'] = 0;
        }
    }
}


int main(){
    
    int visited[26];
    
    for (int i=0; i<26; i++) visited[i] = 0;
    
    scanf("%d %d", &R, &C);
    
    for (int i=0; i<R; i++) scanf("%s", &board[i][0]);
    
    visited[board[0][0] - 'A'] = 1;
    
    dfs(0, 0, visited, 1);
    
    printf("%d\n", answer);
    
    
    return 0;
    
}