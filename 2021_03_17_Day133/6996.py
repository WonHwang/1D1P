# 1D1P Day133 BOJ 6996번 아나그램 문제 - 2021.03.17

T = int(input())
for _ in range(T):

    a, b = input().split()

    for_a = [0] * 26
    for_b = [0] * 26

    for char in a:
        for_a[ord(char) - ord('a')] += 1
    
    for char in b:
        for_b[ord(char) - ord('a')] += 1
    
    answer = True

    for i in range(26):
        if for_a[i] != for_b[i]:
            answer = False
            break
    
    print(f"{a} & {b} are ", end="")
    print("anagrams." if answer else "NOT anagrams.")