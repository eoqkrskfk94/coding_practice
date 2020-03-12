import sys
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
T = int(sys.stdin.readline())


def bfs(y, x):

  queue = [[y,x]]
  while(queue):

    i, j = queue[0][0], queue[0][1]
    queue.pop(0)

    for dir in range(4):
      q = i + dy[dir]
      w = j + dx[dir]

      if 0 <= q < N and 0 <= w < M and bat[q][w] == 1:
        bat[q][w] = 0
        queue.append([q,w])

  
  
answer = []

for i in range(T):
  M, N, K = map(int,sys.stdin.readline().split())
  bat = [[0] * M for i in range(N)]

  for i in range(K):
    x, y = map(int,sys.stdin.readline().split())
    bat[y][x] = 1

  count = 0
  for i in range(N):
    for j in range(M):
      if bat[i][j] == 1:
        bfs(i, j)
        bat[i][j] = 0
        count += 1
  
  answer.append(count)


for ans in answer:
  print(ans)






