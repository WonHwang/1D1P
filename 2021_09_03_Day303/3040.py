# 1D1P Day303 BOJ 3040번 백설공주와 일곱 난장이 문제 - 2021.09.03

answer = 0

nums = []

for _ in range(9):
    nums.append(int(input()))

def dfs(target, idx):

    global answer

    if len(target) == 7:
        if sum(target) == 100:
            answer = 1
            for i in range(7):
                print(target[i])
        return
    
    if idx == 9 or answer:
        return

    target.append(nums[idx])
    dfs(target, idx+1)
    target.pop()
    dfs(target, idx+1)

dfs([], 0)