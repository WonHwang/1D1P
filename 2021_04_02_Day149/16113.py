# 1D1P Day149 BOJ 16113번 시그널 문제 - 2021.04.02

from sys import stdin
input = stdin.readline

number = {
    '###\n#.#\n#.#\n#.#\n###' : '0',
    '#\n#\n#\n#\n#' : '1',
    '###\n..#\n###\n#..\n###' : '2',
    '###\n..#\n###\n..#\n###' : '3',
    '#.#\n#.#\n###\n..#\n..#' : '4',
    '###\n#..\n###\n..#\n###' : '5',
    '###\n#..\n###\n#.#\n###' : '6',
    '###\n..#\n..#\n..#\n..#' : '7',
    '###\n#.#\n###\n#.#\n###' : '8',
    '###\n#.#\n###\n..#\n###' : '9',
}

blank = '.\n.\n.\n.\n.'

target = []
N = int(input())
string = input().rstrip()
for i in range(1, 6):
    target.append(string[(N//5)*(i-1):(N//5)*i])

idx = 0
answer = ''
while idx < N//5:

    if target[0][idx] == '.':
        idx += 1
        continue

    if idx == N//5 - 1:
        answer += '1'
        break

    if target[0][idx+1]=='.' and target[4][idx]=='#':
        answer += '1'
        idx += 1
        continue
    
    tmp = ''
    for i in range(5):
        tmp += target[i][idx:idx+3]
        tmp += '\n'

    answer += number[tmp[:-1]]
    idx += 3

print(answer)