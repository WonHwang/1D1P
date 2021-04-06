# 1D1P Day153 BOJ 18870번 좌표 압축 문제 - 2021.04.06

N = int(input())
numbers = list(map(int, input().split()))
number_set = list(set(numbers))
number_set.sort(reverse=True)
answer_dict = {}
tmp = len(number_set) - 1
for num in number_set:
    answer_dict[num] = tmp
    tmp -= 1

answer = [0] * N
for i in range(N):
    answer[i] = answer_dict[numbers[i]]

print(*answer)