import sys

N = int(sys.stdin.readline())
sign = sys.stdin.readline()
M = int(sys.stdin.readline())

if sign == "*\n":
    print(N * M)
else:
    print(N + M)
