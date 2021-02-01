for t in range(1, 11):
    T = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    
    maxi = 0

    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[i][j]
        if tmp > maxi:
            maxi = tmp
    
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[j][i]
        if tmp > maxi:
            maxi = tmp
    
    cross1 = 0
    cross2 = 0
    for i in range(100):
        cross1 += arr[i][i]
        cross2 += arr[i][99-i]
    
    if cross1 > maxi:
        maxi = cross1
    if cross2 > maxi:
        maxi = cross2
    
    print(f"#{t} {maxi}")