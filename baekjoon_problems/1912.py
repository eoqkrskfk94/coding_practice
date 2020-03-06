import sys

N = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split()))
max_num = []

if num[0] >= 0:
  max_num.append(num[0])
else:
  max_num.append(-1)

for i in range(1,N):
  if num[i] >= 0:
    if max_num[i-1] == -1:
      max_num.append(num[i])
    else:
      max_num.append(max_num[i-1] + num[i])
  elif num[i] < 0:
    if max_num[i-1] + num[i] > 0:
      max_num.append(max_num[i-1] + num[i])
    else:
      max_num.append(-1)


#print(max_num)
if max(max_num) < 0:
  print(max(num))
else:
  print(max(max_num))

