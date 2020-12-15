# 1D1P Day41 BOJ 10610번 30 문제 - 2020.12.15

N = input()

arr = []
existence_0 = 0
summation = 0
for i in range(len(N)):
    if N[i] == '0':
        existence_0 = 1
    summation += int(N[i])
    arr.append(N[i])

if existence_0 == 1 and summation % 3 == 0:
    arr.sort(reverse = True)
    answer = ""
    for i in range(len(arr)):
        answer += arr[i]
    print(answer)

else:
    print(-1)