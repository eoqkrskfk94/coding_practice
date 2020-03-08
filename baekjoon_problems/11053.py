import sys

N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

max_len = [1] * N

#max_len[0] = 1

for i in range(1,N):
  for j in range (i):
    if num[i] > num[j]:
      max_len[i] = max(max_len[i], max_len[j] + 1)


print(max(max_len))

