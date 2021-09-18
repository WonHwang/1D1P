# 1D1P Day318 BOJ 1145번 적어도 대부분의 배수 문제 - 2021.09.18

nums = list(map(int, input().split()))

answer = min(nums)

while True:
    cnt = 0

    for num in nums:
        if not answer % num:
            cnt += 1
    
    if cnt >= 3:
        break
    
    answer += 1

print(answer)