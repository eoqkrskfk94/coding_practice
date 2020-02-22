import sys

N, M = sys.stdin.readline().split()

start = []
answer = []
diff = []
for i in range(int(N)):
  temp = list(sys.stdin.readline())
  start.append(temp[:-1])

for i in range(int(N)):
  temp = list(sys.stdin.readline())
  answer.append(temp[:-1])
  temp2 = []
  for j in range(int(M)):
    if start[i][j] == temp[j]:
      temp2.append('T')
    else:
      temp2.append('F')
  diff.append(temp2)

#print(diff)
count = 0

for i in range(int(N)-2):
  for j in range(int(M)-2):
    if diff[i][j] == 'F':
      count += 1
      for x in range(3):
        for y in range(3):
          if diff[i+x][j+y] == 'F':
            diff[i+x][j+y] = 'T'
          else:
            diff[i+x][j+y] = 'F'

correct = 1
for i in range(int(N)):
  for j in range(int(M)):
    if diff[i][j] == 'F':
      correct = 0
      break

if correct == 1:
  print(count)
else:
  print(-1)



    

