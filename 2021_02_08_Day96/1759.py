# 1D1P Day96 BOJ 1759번 암호 만들기 문제 - 2021.02.08

from sys import stdin

L, C = map(int, stdin.readline().rstrip().split())

words = stdin.readline().rstrip().split()
words.sort()

visited = [0] * (C+1)

vowels = ['a', 'e', 'i', 'o', 'u']

def combination(result, n, r, depth):

    if len(result) == r:
        answer = ""
        for num in result:
            answer += words[num]
        
        howmany_vowel = 0
        for vowel in vowels:
            if vowel in answer:
                howmany_vowel += 1
        
        if howmany_vowel >= 1 and r - howmany_vowel >= 2:
            print(answer)
    
    for i in range(depth, n):
        if visited[i] == 0:
            result.append(i)
            visited[i] = 1
            combination(result, n, r, i)
            visited[result.pop()] = 0


combination([], C, L, 0)