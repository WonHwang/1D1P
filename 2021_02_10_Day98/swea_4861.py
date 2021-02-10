for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    strings = []
    for i in range(N):
        strings.append(input())
    
    strings_transpose = []
    for i in range(N):
        tmp = ""
        for j in range(N):
            tmp += strings[j][i]
        strings_transpose.append(tmp)
    
    answer = 0

    for i in range(N):
        for j in range(N-M+1):
            tmp = strings[i][j:j+M]
            if tmp == tmp[::-1]:
                answer = tmp
                break
        if answer:
            break
    
    if not answer:
        for i in range(N):
            for j in range(N-M+1):
                tmp = strings_transpose[i][j:j+M]
                if tmp == tmp[::-1]:
                    answer = tmp
                    break
            if answer:
                break
    
    print(f"#{tc} {answer}")