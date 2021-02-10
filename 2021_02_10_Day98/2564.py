# 1D1P Day98 BOJ 2564번 경비원 문제 - 2021.02.10

W, H = map(int, input().split())
N = int(input())
shop = []
for i in range(N):
    shop.append(list(map(int, input().split())))
position = list(map(int, input().split()))

distance = [0] * N

for i in range(N):
    tmp = shop[i]
    if position[0] == tmp[0]:
        distance[i] = tmp[1] - position[1] if tmp[1] > position[1] else position[1] - tmp[1]
    
    elif (position[0] == 1 and tmp[0] == 2) or (position[0] == 2 and tmp[0] == 1):
        case1 = position[1] + H + tmp[1]
        case2 = (W - position[1]) + H + (W - tmp[1])
        distance[i] = case1 if case1 < case2 else case2

    elif (position[0] == 1 and tmp[0] == 3) or (position[0] == 3 and tmp[0] == 1):
        distance[i] = position[1] + tmp[1]
    
    elif position[0] == 1 and tmp[0] == 4:
        distance[i] = (W - position[1]) + tmp[1]
    
    elif position[0] == 4 and tmp[0] == 1:
        distance[i] = (W - tmp[1]) + position[1]
    
    elif position[0] == 2 and tmp[0] == 3:
        distance[i] = position[1] + (H - tmp[1])
    
    elif position[0] == 3 and tmp[0] == 2:
        distance[i] = (H - position[1]) + tmp[1]
    
    elif position[0] == 2 and tmp[0] == 4:
        distance[i] = (W - position[1]) + (H - tmp[1])
    
    elif position[0] == 4 and tmp[0] == 2:
        distance[i] = (H - position[1]) + (W - tmp[1])
    
    elif (position[0] == 3 and tmp[0] == 4) or (position[0] == 4 and tmp[0] == 3):
        case1 = W + position[1] + tmp[1]
        case2 = W + (H - position[1]) + (H - tmp[1])
        distance[i] = case1 if case1 < case2 else case2
    
answer = 0

for i in range(N):
    answer += distance[i]

print(answer)