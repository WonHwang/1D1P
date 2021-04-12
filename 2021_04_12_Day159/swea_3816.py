# 1D1P Day159 SWEA 3816번 아나그램 문제 - 2021.04.12

for tc in range(1, int(input())+1):

    s1, s2 = map(str, input().split())

    s1_count = [0] * 26

    for char in s1:
        s1_count[ord(char) - ord('a')] += 1
    
    s2_count = [0] * 26
    for i in range(len(s1)):
        s2_count[ord(s2[i]) - ord('a')] += 1
    answer = 0

    if s1_count == s2_count:
        answer += 1
    
    for i in range(len(s2) - len(s1)):
        s2_count[ord(s2[i]) - ord('a')] -= 1
        s2_count[ord(s2[i+len(s1)]) - ord('a')] += 1

        if s1_count == s2_count:
            answer += 1
        
    print(f"#{tc} {answer}")