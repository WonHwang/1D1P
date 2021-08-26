# 아 푼거네...

A_set = []
B_set = []

def findAllCase(N, L, idx, now, kind):

    if idx == L:
        if kind == 'A':
            A_set.append(int(now))
            return
        else:
            B_set.append(int(now))
            return
    
    if N[idx] == '5' or N[idx] == '6':
        findAllCase(N, L, idx+1, now+'5', kind)
        findAllCase(N, L, idx+1, now+'6', kind)
    
    else:
        findAllCase(N, L, idx+1, now+N[idx], kind)


A, B = map(str, input().split())
findAllCase(A, len(A), 0, '', 'A')
findAllCase(B, len(B), 0, '', 'B')

print(min(A_set) + min(B_set), max(A_set) + max(B_set))