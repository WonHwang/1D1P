N = int(input())
times = []

for _ in range(N):
    tmp = input().split(' ~ ')
    start = tmp[0].split(':')
    end = tmp[1].split(':')
    
    tmp = []
    h, m = map(int, start)
    tmp.append(60*h + m)
    h, m = map(int, end)
    tmp.append(60*h + m)

    times.append(tmp)

Min, Max = 60*24, 0

for i in range(N):
    if times[i][1] < Min:
        Min = times[i][1]
    if times[i][0] > Max:
        Max = times[i][0]

start = f"{str(Max//60).zfill(2)}:{str(Max%60).zfill(2)}"
end = f"{str(Min//60).zfill(2)}:{str(Min%60).zfill(2)}"

print(f"{start} ~ {end}" if Min > Max else -1)