import sys

N = int(sys.stdin.readline())

board = []
new_board = [[0] * N for i in range(N)]

for i in range(N):
  board.append(list(map(int,sys.stdin.readline().split())))


def dfs(idx, y, x):

  new_board[idx][x] = 1
  for i in range(N):
    if new_board[idx][i] == 0 and board[x][i] == 1:
      dfs(idx, x, i)

      




for i in range(N):
  for j in range(N):
    if new_board[i][j] == 0 and board[i][j] == 1:
      dfs(i, i, j)

    


for i in range(N):
  for j in range(N):
    print(new_board[i][j], end= " ")
  print()



