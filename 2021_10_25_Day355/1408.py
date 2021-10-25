# 1D1P Day355 BOJ 1408번 24 문제 - 2021.10.25

def toSec(h, m, s):

    return 60*60*h + 60*m + s

def toHour(sec):
    h = sec // (60*60)
    sec %= 60*60
    m = sec // 60
    s = sec % 60

    return h, m, s

sh, sm, ss = map(int, input().split(':'))
eh, em, es = map(int, input().split(':'))

start, end = toSec(sh, sm, ss), toSec(eh, em, es)

if end >= start:
    sec = end - start
else:
    sec = 24*60*60 - (start-end)

h, m, s = toHour(sec)
print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")