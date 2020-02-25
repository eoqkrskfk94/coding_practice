import sys

N = sys.stdin.readline()

new_num = []

temp = N[0]
for i in range(1,len(N)):
  if temp == N[i]:
    continue
  else:
    new_num.append(temp)
    temp = N[i]


count_0 = new_num.count('0')


if count_0 < len(new_num) - count_0:
  print(count_0)
else:
  print(len(new_num) - count_0)

