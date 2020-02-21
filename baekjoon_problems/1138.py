import sys
N = sys.stdin.readline()
M = list(map(int,sys.stdin.readline().split()))

line = [0] * len(M)

#print(M, line)

for i in range(len(M)):
  temp = M[i]
  for j in range(len(line)):
    if temp == 0 and line[j] == 0:
      line[j] = i+1
      break
    elif line[j] == 0:
      temp -= 1
  #print(line)


for i in line:
  print(i, end = " ")





