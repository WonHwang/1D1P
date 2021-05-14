# 1D1P Day191 BOJ 4613번 QuickSum 문제 - 2021.05.14

while True:
    string = input()
    if string == '#':
        break

    answer = 0
    for i in range(len(string)):
        if string[i] == ' ':
            continue

        answer += (i+1) * (ord(string[i]) - ord('A') + 1)
    
    print(answer)