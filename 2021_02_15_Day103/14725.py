# 1D1P Day103 BOJ 14725번 개미굴 문제 - 2021.02.15

from sys import stdin
from collections import deque

input = stdin.readline

class Node:

    def __init__(self, key):
        self.key = key
        self.children = {}
        self.children_list = []

class Trie:

    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
                current_node.children_list.append(char)
            current_node = current_node.children[char]
    
    def dosort(self):
        queue = deque()
        queue.append(self.head)
        while queue:
            node = queue.popleft()
            node.children_list.sort()
            for child in node.children:
                queue.append(node.children[child])
    
    def print(self, node, depth):
        
        if node.key:
            for i in range(depth):
                print('--', end = '')
            print(node.key)
        for child in node.children_list:
            self.print(node.children[child], depth + 1)

N = int(input())
trie = Trie()
for i in range(N):
    input_ = input().rstrip().split()
    trie.insert(input_[1:])
trie.dosort()
trie.print(trie.head,-1)
