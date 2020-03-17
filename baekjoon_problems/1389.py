import sys

N, M = map(int,sys.stdin.readline().split())
tree = [[N] * N for i in range(N)]

answer = M

for i in range(M):
  x , y = map(int,sys.stdin.readline().split())
  tree[x-1][y-1] = 1
  tree[y-1][x-1] = 1


for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == j:
        tree[i][j] = 0
      else:
        tree[i][j] = min(tree[i][j], tree[i][k] + tree[k][j])



answer = []
person = N
for i in range(N):
  answer.append(sum(tree[i]))


print(answer.index(min(answer))+1)



  




