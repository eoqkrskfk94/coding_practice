import sys

top = []
for i in range(4):
  top.append(list(sys.stdin.readline().rstrip()))


N = int(sys.stdin.readline())

T = []

for i in range(N):
  T.append(list(map(int,sys.stdin.readline().split())))


def move_clock(gear):
  temp = gear.pop()
  gear.insert(0,temp)

def move_clockwise(gear):
  temp = gear.pop(0)
  gear.append(temp)


for i in range(N):
  top_n = T[i][0]-1

  connect = [0,0,0]
  direction = [0,0,0,0]

  for j in range(3):
    if top[j][2] != top[j+1][6]:
      connect[j] = 1

  direction[top_n] = T[i][1]

  if top_n -1 >= 0:
    for j in range(top_n-1,-1,-1):

      if connect[j] == 0:
        break
      elif connect[j] == 1:
        direction[j] = direction[j+1] * -1

  if top_n + 1 < 4:
    for j in range(top_n+1,4):
      
      if connect[j-1] == 0:
        break
      elif connect[j-1] == 1:
        direction[j] = direction[j-1] * -1
  
  for i in range(4):
    if direction[i] == 1:
      move_clock(top[i])
    elif direction[i] == -1:
      move_clockwise(top[i])
      
  

answer = 0

if top[0][0] == '1':
  answer += 1
if top[1][0] == '1':
  answer += 2
if top[2][0] == '1':
  answer += 4
if top[3][0] == '1':
  answer += 8

print(answer)





