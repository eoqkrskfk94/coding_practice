import sys

N, M = sys.stdin.readline().split()
N, M = int(N), int(M)

pipes = list(map(int,sys.stdin.readline().split()))
pipes.sort()

start = pipes[0]
tapes = 1
for i in range(1,N):
  if start + M - 1 < pipes[i]:
    tapes += 1
    start = pipes[i]

print(tapes)
