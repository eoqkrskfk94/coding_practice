import sys

N = int(sys.stdin.readline())

M = list(map(int,sys.stdin.readline().split()))

count = 0
for car in M:
    if car == N:
        count += 1

print(count)
