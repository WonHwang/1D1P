# 1D1P Day251 BOJ 20154번 이 구역의 승자는 누구야?! 문제 - 2021.07.13

lines = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 3,
    'F': 3,
    'G': 3,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 3,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 2,
    'X': 2,
    'Y': 2,
    'Z': 1
}

def daq(string):

    if len(string) == 1:
        return lines[string[0]]
    
    return (daq(string[:len(string)//2]) + daq(string[len(string)//2:])) % 10

string = list(input())

answer = daq(string)

print("I'm a winner!" if answer%2 else "You're the winner?")