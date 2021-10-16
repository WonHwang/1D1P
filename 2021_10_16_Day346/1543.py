# 1D1P Day346 BOJ 1543번 문서 검색 문제 - 2021.10.16

string = input()
target = input()
N = len(target)

answer = 0
idx = 0
while idx < len(string)-N+1:

    if string[idx:idx+N] == target:
        answer += 1
        idx += N
        continue

    idx += 1

print(answer)