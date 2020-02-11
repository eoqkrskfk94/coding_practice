x, y = map(str,input().split(" "))

minum = len(x)
for i in range(len(y) - len(x) + 1):
    diff = 0
    for j in range(len(x)):
        if y[i+j] != x[j]:
            diff += 1
    minum = min(minum, diff)


print(minum)
