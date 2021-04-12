# 1D1P Day159 SWEA 1240번 단순 2진 암호코드 문제 - 2021.04.12
# SWEA 최악의 문제

password = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())

    code = []
    for _ in range(N):
        code.append(input())
    
    decode_list = []

    for i in range(N):
        for j in range(0, M-7+1):

            if code[i][j:j+7] in password:
                for k in range(j, j+56, 7):
                    try:
                        decode_list.append(password[code[i][k:k+7]])
                    except:
                        decode_list = []
                        break
                
                if decode_list:
                    break
        if decode_list:
            break
    print(f"#{tc} ", end='')
    
    if len(decode_list) == 8:

        total = 0

        for i in range(0, 8, 2):
            total += 3 * decode_list[i]
        
        for i in range(1, 8, 2):
            total += decode_list[i]

        if not total%10:
            print(sum(decode_list))
    
        else:
            print(0)
    else:
        print(0)