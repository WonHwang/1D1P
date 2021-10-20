# 1D1P Day350 BOJ 1919번 애너그램 만들기 문제 - 2021.10.20

def count(string):
    arr = [0] * 26
    for i in range(ord('a'), ord('z')+1):
        cnt = 0
        for digit in string:
            if digit == chr(i):
                cnt += 1
        arr[i-ord('a')] = cnt
    
    return arr

a = list(input())
b = list(input())
a.sort()
b.sort()
a_count = count(a)
b_count = count(b)

answer = 0
for i in range(26):
    answer += abs(a_count[i] - b_count[i])

print(answer)