import sys

N = int(sys.stdin.readline())


board = []
count = [0]
for i in range(N):
  board.append(sys.stdin.readline().rstrip())

new_board = [[0] * N for i in range(N)]

def solve(new_board,board,y,x,idx):

  if y < 0 or y >= N or x < 0 or x >= N:
    return

  if int(board[y][x]) == 0:
    return
  if int(new_board[y][x]) != 0:
    return

  if int(board[y][x]) == 1:
    new_board[y][x] = idx
    count[-1] += 1
    flag = 1
  
  solve(new_board,board,y-1,x,idx)
  solve(new_board,board,y+1,x,idx)
  solve(new_board,board,y,x-1,idx)
  solve(new_board,board,y,x+1,idx)


  return flag
number = 1
for i in range(N):
  for j in range(N):
    idx = solve(new_board,board,i,j,number)
    if idx == 1:
      number += 1
      count.append(0)
      
# for i in range(N):
#   print(new_board[i])
count.pop()
count.sort()
print(number-1)
for i in range(number-1):
  print(count[i])





