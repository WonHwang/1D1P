# 1D1P Day162 BOJ 14225번 부분수열의 합 문제 - 2021.04.15

def makesubset(total, idx):

    if idx == N:
        subset[total] = 1
        return
    
    makesubset(total+numbers[idx], idx+1)
    makesubset(total, idx+1)

N = int(input())
numbers = list(map(int, input().split()))
subset = dict()
makesubset(0, 0)
for i in range(1, 2000001):
    if not subset.get(i):
        answer = i
        break

print(i)