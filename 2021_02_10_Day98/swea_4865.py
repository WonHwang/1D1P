# 1D1P Day98 SWEA 4865번 글자수 문제 - 2021.02.10

for tc in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()

    dict1 = {}
    dict2 = {}

    for i in range(len(str1)):
        dict1[str1[i]] = dict1.get(str1[1], 0) + 1
    
    for i in range(len(str2)):
        dict2[str2[i]] = dict2.get(str2[i], 0) + 1
    
    Max = 0
    for key in dict1:
        if dict2.get(key) and dict2[key] > Max:
            Max = dict2[key]
    
    print(f"#{tc} {Max}")