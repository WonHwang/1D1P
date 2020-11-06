# 1D1P Day2 BOJ 2108번 통계학 문제 - 2020.11.06
import sys

N = int(input())
arr = [0] * N
summation = 0
howmany = [0] * 8001
maximum = -4000
minimum = 4000
mostbeen = 0
mostbeen_index = 0

for i in range(N):
    arr[i] = int(sys.stdin.readline())
    summation += arr[i]
    if arr[i] >= maximum:
        maximum = arr[i]
    if arr[i] <= minimum:
        minimum = arr[i]

for number in arr:
    if number >= 0:
        howmany[number] += 1
    else:
        howmany[8001 + number] += 1

for i in range(8001):
    if howmany[i] > mostbeen:
        mostbeen = howmany[i]

flag = 0
for i in range(4001, 8001):
    if flag == 2:
        break
    if howmany[i] == mostbeen:
        mostbeen_index = i
        flag += 1

for i in range(0, 4001):
    if flag == 2:
        break
    if howmany[i] == mostbeen:
        mostbeen_index = i
        flag += 1

if mostbeen_index > 4000:
    mostbeen_index -= 8001

arr.sort()

mid = int(N/2)
midvalue = arr[mid]

print(round(summation / N))
print(midvalue)
print(mostbeen_index)
print(maximum - minimum)