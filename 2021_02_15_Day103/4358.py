import sys
input = sys.stdin.readline

trees = {}

total = 0
while True:
    tmp = input().rstrip()
    if not tmp:
        break
    trees[tmp] = trees.get(tmp, 0) + 1
    total += 1
    
tree_list = []

for key in trees:
    rate = (trees[key] / total) * 100
    tree_list.append([key, rate])

tree_list.sort(key = lambda x : x[0])

for tree in tree_list:
    print("%s %.4f"%(tree[0], tree[1]))