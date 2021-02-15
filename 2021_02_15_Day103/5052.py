# 1D1P Day103 BOJ 5052번 전화번호 목록 문제 - 2021.02.15

from sys import stdin

class Node:

    def __init__(self, key, data = None):

        self.key = key
        self.data = data
        self.children = {}

class Trie:

    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):

        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            
            current_node = current_node.children[char]
        
        current_node.data = string

    def search(self, string):

        current_node = self.head

        for char in string:
            if char not in current_node.children:
                return False
            
            current_node = current_node.children[char]
        
        if current_node.data:
            return True
    
    def is_valid(self, string):

        current_node = self.head

        for char in string:
            if char not in current_node.children:
                return False
            
            current_node = current_node.children[char]
        
        if current_node.data and current_node.children:
            return True


for tc in range(int(stdin.readline())):

    N = int(stdin.readline())

    number_list = []
    
    for i in range(N):
        number_list.append(stdin.readline().rstrip())
    
    trie = Trie()

    for i in range(N):
        trie.insert(number_list[i])
    
    answer = True
    for i in range(N):
        if trie.is_valid(number_list[i]):
            answer = False
            break
    
    print("YES" if answer else "NO")