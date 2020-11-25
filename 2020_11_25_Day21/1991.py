# 1D1P Day21 BOJ 1991번 트리 순회 문제 - 2020.11.25

from collections import deque

N = int(input())

tree = dict()

for i in range(N):
    node, left, right = map(str, input().split(' '))
    tree[node] = [left, right]

preorder_traversal = []

def preorder(node):
    preorder_traversal.append(node)
    left = tree[node][0]
    right = tree[node][1]

    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

preorder('A')
answer = ""
for i in preorder_traversal:
    answer += i
print(answer)

inorder_traversal = []

def inorder(node):
    left = tree[node][0]
    right = tree[node][1]

    if left != '.':
        inorder(left)
    inorder_traversal.append(node)
    if right != '.':
        inorder(right)

inorder('A')
answer = ""
for i in inorder_traversal:
    answer += i
print(answer)

postorder_traversal = []

def postorder(node):
    
    left = tree[node][0]
    right = tree[node][1]

    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    postorder_traversal.append(node)

postorder('A')
answer = ""
for i in postorder_traversal:
    answer += i
print(answer)