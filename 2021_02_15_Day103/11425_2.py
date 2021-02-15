# 1D1P Day103 BOJ 11425번 문자열 집합 문제 Trie 풀이 - 2021.02.15
# Python - 시간 초과, Pypy - 통과

class Node:

    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:

    def __init__(self):
        self.head_node = Node(None)
    
    def insert(self, string):
        current_node = self.head_node

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            
            current_node = current_node.children[char]
        
        current_node.data = string
    
    def find(self, string):
        current_node = self.head_node

        for char in string:
            if char not in current_node.children:
                return 0
            
            current_node = current_node.children[char]
        
        if current_node.data:
            return 1
        return 0

from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())

strings = []

for i in range(N):
    strings.append(stdin.readline().rstrip())

trie = Trie()
for i in range(N):
    trie.insert(strings[i])

answer = 0
for i in range(M):
    answer += trie.find(stdin.readline().rstrip())

print(answer)