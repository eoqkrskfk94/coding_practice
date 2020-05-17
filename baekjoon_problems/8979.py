import sys

N, M = map(int,sys.stdin.readline().split())

countries = []
idx = []


for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    if temp[0] == M:
        idx = temp
    else:
        countries.append(temp)


count = 0

for i in range(N-1):
    if idx[1] < countries[i][1]:
        count += 1
        continue

    elif idx[1] == countries[i][1]:
        if idx[2] < countries[i][2]:
            count += 1
            continue

        elif idx[2] == countries[i][2]:
            if idx[3] < countries[i][3]:
                count += 1
                continue


print(count+1)
