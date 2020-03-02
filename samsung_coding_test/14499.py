import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())
maps = []
for i in range(N):
  maps.append(list(map(int,sys.stdin.readline().split())))

order = list(map(int,sys.stdin.readline().split()))

dice = [0,0,0,0,0,0]
dice_top = []
loc = [x,y]

def move_dice(direction):
  new_dice = [0,0,0,0,0,0]
  if direction == 1:
    new_dice[0] = dice[0]
    new_dice[5] = dice[1]
    new_dice[2] = dice[2]
    new_dice[4] = dice[3]
    new_dice[1] = dice[4]
    new_dice[3] = dice[5]
  elif direction == 2:
    new_dice[0] = dice[0]
    new_dice[4] = dice[1]
    new_dice[2] = dice[2]
    new_dice[5] = dice[3]
    new_dice[3] = dice[4]
    new_dice[1] = dice[5]
  elif direction == 3:
    new_dice[3] = dice[0]
    new_dice[0] = dice[1]
    new_dice[1] = dice[2]
    new_dice[2] = dice[3]
    new_dice[4] = dice[4]
    new_dice[5] = dice[5]
  elif direction == 4:
    new_dice[1] = dice[0]
    new_dice[2] = dice[1]
    new_dice[3] = dice[2]
    new_dice[0] = dice[3]
    new_dice[4] = dice[4]
    new_dice[5] = dice[5]
  return new_dice



for k in order:
  if k == 1:
    if loc[1]+1 >= M:
      continue
    loc[1] += 1

  elif k == 2:
    if loc[1]-1 < 0:
      continue
    loc[1] -= 1

  elif k == 3:
    if loc[0]-1 < 0:
      continue  
    loc[0] -= 1

  elif k == 4:
    if loc[0]+1 >= N:
      continue
    loc[0] += 1
  
  dice = move_dice(k)

  if maps[loc[0]][loc[1]] == 0:
    maps[loc[0]][loc[1]] = dice[3] 
  else:
    dice[3] = maps[loc[0]][loc[1]]
    maps[loc[0]][loc[1]] = 0
  
  print(dice[1])
