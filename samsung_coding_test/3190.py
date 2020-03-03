import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = [[0] * (N+1) for i in range(N+1)]

for i in range(K):
  x, y = sys.stdin.readline().split()
  x ,y = int(x), int(y)
  apples[x][y] = 1

L = int(sys.stdin.readline())

# movement = [''] * 101
# for i in range(L):
#   sec, direc = sys.stdin.readline().split()
#   movement[int(sec)] = direc

movement = {}
for i in range(L):
  sec, direc = sys.stdin.readline().split()
  movement[int(sec)] = direc





snake = [[0] * (N+1) for i in range(N+1)]
snake[1][1] = 1
head_x, head_y = 1 , 1
tail = [[1,1]]
time = 0
direc = 0


dy = [0, +1, 0, -1]
dx = [+1, 0, -1, 0]

while True:
  time += 1
  head_y += dy[direc]
  head_x += dx[direc]

  if head_y > N or head_x > N or head_y < 1 or head_x < 1 or snake[head_y][head_x] == 1:
    break

  snake[head_y][head_x] = 1
  tail.insert(0, [head_y, head_x])

  if apples[head_y][head_x] == 0:
    y, x = tail.pop()
    snake[y][x] = 0
  
  if apples[head_y][head_x] == 1:
    apples[head_y][head_x] = 0

  if time in movement:
    if movement[time] == 'D':
      direc = (direc + 1) % 4
    elif movement[time] == 'L':
      direc = (direc + 3) % 4 


print(time)




