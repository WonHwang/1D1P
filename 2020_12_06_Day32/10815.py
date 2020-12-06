# 1D1P Day32 BOJ 10815번 숫자 카드 문제 - 2020.12.06

from sys import stdin

N = int(stdin.readline().rstrip())

numbers = stdin.readline().rstrip().split(' ')

for i in range(N):
    numbers[i] = int(numbers[i])

M = int(stdin.readline().rstrip())

targets = stdin.readline().rstrip().split(' ')

answer = ""
numbers.sort()

for _ in range(M):
    target = int(targets[_])
    front = 0
    end = N-1

    while front <= end:
        mid = (front + end) // 2

        if numbers[mid] == target:
            break

        elif numbers[mid] > target:
            end = mid - 1
        
        else:
            front = mid + 1
            
    if numbers[mid] == target:
        answer += str(1) + " "
    
    else:
        answer += str(0) + " "

print(answer[:-1])