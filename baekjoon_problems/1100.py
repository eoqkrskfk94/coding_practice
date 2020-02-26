import sys

total = 0
chess = []
for i in range(8):
  chess.append(sys.stdin.readline().rstrip())

#print(chess)

for i in range(8):
  if i % 2 == 0:
    for j in range(8):
      if j % 2 == 0:
        if chess[i][j] == 'F':
          total += 1
  else:
    for j in range(8):
      if j % 2 != 0:
        if chess[i][j] == 'F':
          total += 1


print(total)
