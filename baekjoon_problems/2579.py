import sys

N = int(sys.stdin.readline())
stair = []
for i in range(N):
  stair += [int(sys.stdin.readline())]

#print(stair)

def solve(stair, N):
  max_step = []
  max_step.append(stair[0])
  max_step.append(stair[0] + stair[1])
  max_step.append(max(stair[2] + stair[1], stair[2] + stair[0]))

  for i in range(3,N):
    max_step.append(max(stair[i] + stair[i-1] + max_step[i-3], stair[i] + max_step[i-2]))

  return max_step
    
  
max_step = solve(stair, N)
print(max_step[-1])


