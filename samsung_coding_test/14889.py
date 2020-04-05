import sys
import copy
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
board = []

for i in range(N):
  board.append(list(map(int,sys.stdin.readline().split())))

used = [0] * N
answer = 1000000
chosen = [0] * N


def check_diff():
  global answer
  score_a = 0
  score_b = 0
  team_a = []
  team_b = []
  for i in range(N):
    if chosen[i] == 1:
      team_a.append(i)
    else:
      team_b.append(i)
  
  for i in range(N//2):
    for j in range(i+1,N//2):
      score_a += (board[team_a[i]][team_a[j]] + board[team_a[j]][team_a[i]])
      score_b += (board[team_b[i]][team_b[j]] + board[team_b[j]][team_b[i]])



  answer = min(answer,abs(score_a-score_b))


def dfs(count,idx):
  if count == N/2:
    check_diff()
    return
  
  for i in range(idx,N):
    if chosen[i]:
      continue
    chosen[i] = 1
    dfs(count+1,i)
    chosen[i] = 0


dfs(0,0)

print(answer)







