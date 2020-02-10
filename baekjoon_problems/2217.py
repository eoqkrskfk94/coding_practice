
n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse = True)

maxim = 0


for i in range(n):
    maxim = max(maxim, ropes[i] * (i+1))


print(maxim)
