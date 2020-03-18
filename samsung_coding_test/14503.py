import sys
dir_y = [-1,0,1,0]
dir_x = [0,1,0,-1]
N, M = map(int,sys.stdin.readline().split())

start = list(map(int,sys.stdin.readline().split()))

board = []

for i in range(N):
  temp = list(map(int,sys.stdin.readline().split()))
  board.append(temp)


def bfs(start,count):
  queue = []
  queue.append(start)
  board[start[0]][start[1]] = 2

  while(queue):
    temp = queue.pop(0)
    y = temp[0]
    x = temp[1]
    current_d = temp[2]

    for i in range(4):
      next_d = ((current_d+3) + (i*3)) % 4
      ny = y + dir_y[next_d]
      nx = x + dir_x[next_d]

      if ny < 0 or ny >= N or nx < 0 or nx >= M or board[ny][nx] != 0:
        continue
      
      board[ny][nx] = count + 2
      count += 1
      queue.append([ny,nx,next_d])
      break
    
    if len(queue) == 0:
      ny = y + (dir_y[current_d] * -1)
      nx = x + (dir_x[current_d] * -1)
      if board[ny][nx] != 1:
        queue.append([ny,nx,current_d])

  return count


count = bfs(start,1)


print(count)




 






