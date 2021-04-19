def multiple(A, X):

    X = bin(X)[2:][::-1]

    tmp = A
    answer = 1
    for i in range(len(X)):
        if X[i] == '1':
            answer = (answer * tmp) % 1000000007
        tmp = (tmp * tmp) % 1000000007
    
    return answer
    
A = int(input())
X = int(input())

print(multiple(A, X))