# 1D1P Day98 SWEA 4843번 특별한 정렬 문제 - 2021.02.10

def countsort(arr):
    count = [0] * 101
    answer = []
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, 101):
        if count[i] != 0:
            while count[i]:
                answer.append(i)
                count[i] -= 1
    return answer
    
for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    sorted_numbers = countsort(numbers)
    reversed_numbers = sorted_numbers[::-1]

    answer = []
    if N % 2:
        for i in range(N // 2):
            answer.append(reversed_numbers[i])
            answer.append(sorted_numbers[i])
        answer.append(sorted_numbers[N // 2])
    else:
        for i in range(N // 2):
            answer.append(reversed_numbers[i])
            answer.append(sorted_numbers[i])
    
    print(f"#{tc}", end = ' ')
    for i in range(10):
        print(answer[i], end = ' ')
    print()