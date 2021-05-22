# 1D1P Day199 BOJ 3059번 등장하지 않는 문자의 합 문제 - 2021.05.22

for tc in range(int(input())):

    arr = [1] * 26
    string = input()
    for digit in string:
        arr[ord(digit) - ord('A')] = 0
    
    answer = 0
    for i in range(26):
        if arr[i]:
            answer += i + 65
    
    print(answer)