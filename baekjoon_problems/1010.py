import sys


def solve(N,M):
  dp = [[0] * M for i in range(M)]

  for i in range(M):
    for j in range(M):
      if i == j:
        dp[i][j] = 1
      elif i == 0:
        dp[i][j] = j+1
      elif i > j:
        dp[i][j] = 0
      else:
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]


  return dp


X = int(sys.stdin.readline())
max_N, max_M = 0, 0
find = []
for i in range(X):
  N, M = map(int, sys.stdin.readline().split())
  find.append([N,M])

  if max_N < N:
    max_N = N
  if max_M < M:
    max_M = M

answer = solve(max_N,max_M)

for i in range(X):
  print(answer[find[i][0]-1][find[i][1]-1])






