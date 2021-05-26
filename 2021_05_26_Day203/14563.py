# 1D1P Day203 BOJ 14563번 완전수 문제 - 2021.05.26

def det(N):
    if N == 1:
        return 'Deficient'

    tmp = [1]

    for i in range(2, int(N ** 0.5) + 1):
        if not N % i:
            tmp.append(i)
            if N//i != i:
                tmp.append(N//i)
    if sum(tmp) == N:
        return 'Perfect'
    elif sum(tmp) > N:
        return 'Abundant'
    else:
        return 'Deficient'

T = int(input())
nums = list(map(int, input().split()))
for i in range(T):
    print(det(nums[i]))