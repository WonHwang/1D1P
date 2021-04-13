'''
K 만큼 차이가 나는게 가능하니?를 이분탐색으로 찾는다.

K 만큼 차이가 나게하고 싶다. 그럼 기울기가 K인 선을 그어서 상한을 판단한다.
이차원배열에다가 각각의 원소가 해당 원소에 영향을 미치는 상한의 값을 저장하면 시간초과날것이다.
따라서 좌에서 한번 우에서 한번 상한을 계산한다.
예를 들어서, 상한 = min(내 상한, 왼쪽 상한 + K)
'''


for tc in range(1, int(input()) + 1):

    N, K = map(int, input().split())

    numbers = list(map(int, input().split()))

    start = 0
    end = (10**9)

    while start < end:

        mid = (start + end) // 2
 

        left_limit = [0] * N
        right_limit = [0] * N

        left_limit[0] = numbers[0]
        right_limit[N-1] = numbers[N-1]

        for i in range(1, N):
            left_limit[i] = min(left_limit[i-1] + mid, numbers[i])
            right_limit[N-1-i] = min(right_limit[N-i] + mid, numbers[N-1-i])

        gap = 0
        for i in range(N):
            limit = min(left_limit[i], right_limit[i])
            if numbers[i] > limit:
                gap += (numbers[i] - limit)

        if gap > K:
            start = mid + 1
            mid += 1
        
        else:
            end = mid
    
    print(f"#{tc} {mid}")