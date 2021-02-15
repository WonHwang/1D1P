# 1D1P Day103 BOJ 5670번 휴대폰 자판 문제 - 2021.02.15

from collections import deque

class Node:

    def __init__(self, key, data = None):

        self.key = key
        self.data = data
        self.number = 0
        self.children = {}

class Trie:

    def __init__(self):
        
        self.head = Node(None)
        self.total = 0
    
    def insert(self, string):
        
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        
        current_node.data = string
    
    def count(self, node, count):

        node.number = count

        if node.data or len(node.children) >= 2:
            count += 1
        
        if node == self.head:
            count = 1
        
        for child in node.children:
            self.count(node.children[child], count)

    def counttotal(self):
        queue = deque()
        queue.append(self.head)

        while queue:
            node = queue.popleft()
            if node.data:
                self.total += node.number
            
            for child in node.children:
                queue.append(node.children[child])

import sys
input = sys.stdin.readline

while True:
    try:
        N = int(input())
        trie = Trie()
        for i in range(N):
            trie.insert(input().rstrip())
        trie.count(trie.head, 0)
        trie.counttotal()
        print("%.2f"%(trie.total / N))
    
    except:
        break