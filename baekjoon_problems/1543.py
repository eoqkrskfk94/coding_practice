import sys

N = str(sys.stdin.readline().rstrip())
M = str(sys.stdin.readline().rstrip())

count = 0
temp = N
idx = 0
while idx < len(N):
  if M not in temp:
    break
  else:
    idx = temp.index(M) + len(M)
    count += 1
    temp = temp[idx:]




print(count)
