import sys
sys.setrecursionlimit(10**6) 
N, M = map(int,sys.stdin.readline().split())
answer = 1000000

board = []
chicken = []
house = []
pick = []

for i in range(N):
  board.append(list(map(int,sys.stdin.readline().split())))
  for j in range(N):
    if board[i][j] == 2:
      chicken.append([i,j])
    elif board[i][j] == 1:
      house.append([i,j])


def check_distance():
  closest = 0
  for i in range(len(house)):
    distance = 100000
    for j in range(len(pick)):
      temp = abs(house[i][0]-pick[j][0]) + abs(house[i][1]-pick[j][1])
      distance = min(distance, temp)
    
    closest += distance

  return closest



def dfs(pos):
  global answer
  if len(pick) == M:
    candi = check_distance()

    answer = min(answer, candi)
    return
  
  for i in range(pos,len(chicken)):
    if chicken[i] not in pick:
      pick.append(chicken[i])
      dfs(i + 1)
      pick.pop()
  

dfs(0)

print(answer)




