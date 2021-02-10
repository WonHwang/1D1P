# 1D1P Day98 BOJ 2621번 카드게임 문제 - 2021.20.10

shape = {'R' : 0, 'B' : 0, 'Y' : 0, 'G' : 0}
count = [0] * 10
number = []

for _ in range(5):
    input_ = input().split()
    shape[input_[0]] += 1
    count[int(input_[1])] += 1
    number.append(int(input_[1]))

number.sort()


shape5 = 0
continuous = 0
same4 = 0
same3andsame2 = 0
justsame3 = 0
same2andsame2 = 0
justsame2 = 0

for key in shape:
    if shape[key] == 5:
        shape5 = 1
        break

if number[0] + 2 == number[1] + 1 == number[2] == number[3] - 1 == number[4] - 2:
    continuous = 1

for i in range(10):
    if count[i] == 4:
        same4 = 1
        break

for i in range(10):
    if count[i] == 3:
        justsame3 = 1
        break

if justsame3:
    for i in range(10):
        if count[i] == 2:
            justsame3 = 0
            same3andsame2 = 1
            break

if not same3andsame2:
    cnt = 0
    for i in range(10):
        if count[i] == 2:
            cnt += 1
    
    if cnt == 2:
        same2andsame2 = 1

    elif cnt == 1:
        justsame2 = 1

if shape5 and continuous:
    score = number[-1] + 900

elif same4:
    for i in range(10):
        if count[i] == 4:
            score = i + 800
            break

elif same3andsame2:
    for i in range(10):
        if count[i] == 3:
            score = i * 10 + 700
            break
    for i in range(10):
        if count[i] == 2:
            score += i
            break

elif shape5:
    score = number[-1] + 600

elif continuous:
    score = number[-1] + 500

elif justsame3:
    for i in range(10):
        if count[i] == 3:
            score = i + 400
            break

elif same2andsame2:
    small = 1
    for i in range(10):
        if count[i] == 2:
            if small:
                score = i + 300
                small = 0
            else:
                score += 10*i

elif justsame2:
    for i in range(10):
        if count[i] == 2:
            score = i + 200

else:
    score = number[-1] + 100

print(score)