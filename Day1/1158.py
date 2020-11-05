# 1D1P Day1 BOJ 1158번 요시푸스 문제 - 2020.11.05

N, K = input().split(' ')
N, K = int(N), int(K)

arr = []
result = []
for i in range(N):
    arr.append(i+1)

while len(arr) > 1:
    index = (K-1) % len(arr)
    result.append(arr[index])
    if index == len(arr):
        arr = arr[:-1]
    else:
        arr = arr[index+1:] + arr[:index]

result.append(arr[0])

answer = '<'
for i in range(N-1):
    answer += (str(result[i]) + ', ')
answer += (str(result[N-1]) + '>')

print(answer)