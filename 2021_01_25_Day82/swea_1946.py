# 1D1P Day82 SWEA 1946번 간단한 압축 풀기 문제 - 2021.01.25

for t in range(1, int(input()) + 1):
    dic = {}
    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = 0
    
    N = int(input())
    result = []
    for i in range(N):
        alpha, num = input().split()
        result += [alpha] * int(num)
    print(f"#{t}")
    for i in range(len(result) // 10 + 1):
        print(''.join(result[10 * i: 10 * (i+1)]))