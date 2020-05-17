import sys

N = int(sys.stdin.readline())

idx = 1
while True:

    if idx * (idx+1)/2 > N:
        break

    idx += 1

print(idx - 1)
