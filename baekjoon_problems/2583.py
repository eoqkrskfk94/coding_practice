import sys
dir_y = [-1,1,0,0]
dir_x = [0,0,-1,1]
sys.setrecursionlimit(100000)
N, M, K = map(int,sys.stdin.readline().split())


rec = []
for i in range(K):
  rec.append(list(map(int,sys.stdin.readline().split())))


board = [[0] * M for i in range(M)]

for k in range(K):
  for i in range(N):
    for j in range(M):
      if rec[k][1] <= i < rec[k][3] and rec[k][0] <= j < rec[k][2]:
        board[i][j] = -1

def spread(y,x, idx):
  if y < 0 or y >= N or x < 0 or x >= M:
    return
  
  if board[y][x] == -1 or board[y][x] == idx:
    return
  if board[y][x] == 0:
    board[y][x] = idx
    flag = 1

  for i in range(4):
    spread(y+dir_y[i],x+dir_x[i],idx)
  
  return flag


idx = 1
for i in range(N):
  for j in range(M):
    if board[i][j] == 0:
      flag = spread(i,j,idx)
      if flag == 1:
        idx += 1

count = [0] * (idx - 1)

for i in range(N):
  for j in range(M):
    if board[i][j] > 0:
      count[board[i][j]-1] += 1

print(len(count))

if len(count) > 0:
  count.sort()

for i in range(len(count)):
  print(count[i], end = " ")


