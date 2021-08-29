# 1D1P Day298 BOJ 3029번 경고 문제 - 2021.08.29

day = 60*60*24

sh, sm, ss = map(int, input().split(':'))
eh, em, es = map(int, input().split(':'))

start = ss + sm*60 + sh*60*60
end = es + em*60 + eh*60*60
time = 0

while start != end:

    time += 1
    start += 1

    if start == day:
        start = 0

fh = time // (3600)
fm = (time % (3600)) // 60
fs = time % (60)

if fh == 0 and fm == 0 and fs == 0:
    fh = 24

fh, fm, fs = str(fh).zfill(2), str(fm).zfill(2), str(fs).zfill(2)

print(f"{fh}:{fm}:{fs}")