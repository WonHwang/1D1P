# 1D1P Day71 SWEA 10912번 외로운 문자 문제 - 2021.01.14

def checkdic(dic):
    result = ""
    for key in dic:
        dic[key] %= 2
        if dic[key] != 0:
            for i in range(dic[key]):
                result += key
    
    if result == "":
        result = "Good"
    return result

T = int(input())

for _ in range(T):

    dic = dict()
    for i in range(ord('a'), ord('z') + 1):
        dic[chr(i)] = 0
    string = input()

    for i in range(len(string)):
        dic[string[i]] += 1
    
    answer = checkdic(dic)
    print("#%d "%(_+1) + answer)