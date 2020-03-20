import sys
dir_y = [0,0,-1,1]
dir_x = [-1,1,0,0]
N = int(sys.stdin.readline())

board = []
shark = []

for i in range(N):
  temp = list(map(int,sys.stdin.readline().split()))
  board.append(temp)
  if 9 in temp:
    shark = [i,temp.index(9),0]

board[shark[0]][shark[1]] = 0

      
shark_size = 2
belly = 0
update = True

while(update):
  update = False

  visit = [[0] * N for i in range(N)]
  queue = [shark]
  visit[shark[0]][shark[1]] = 1
  candi_y, candi_x = 20, 20
  candi_t = -1

  while(queue):
    cur = queue.pop(0)
    cur_y = cur[0]
    cur_x = cur[1]
    cur_t = cur[2]

    if candi_t != -1 and candi_t < cur_t:
      break

    if board[cur_y][cur_x] < shark_size and board[cur_y][cur_x] != 0:
      update = True 
      if candi_y > cur_y or (candi_y == cur_y and candi_x > cur_x):
        candi_y, candi_x, candi_t = cur_y, cur_x, cur_t

    for i in range(4):
      ny = cur_y + dir_y[i]
      nx = cur_x + dir_x[i]
      nt = cur_t + 1

      if ny < 0 or ny >= N or nx < 0 or nx >= N:
        continue
      
      if visit[ny][nx] == 0 and shark_size >= board[ny][nx]:
        visit[ny][nx] = 1
        queue.append([ny,nx,nt])

  if(update):
    shark = [candi_y,candi_x,candi_t]
    belly += 1
    if belly == shark_size:
      shark_size += 1
      belly = 0
  
    board[shark[0]][shark[1]] = 0

print(shark[2])

  

