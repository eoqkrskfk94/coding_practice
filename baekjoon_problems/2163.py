import sys

N, M = map(int, sys.stdin.readline().split())

dp = [0] * (N*M+1)


for i in range(1,N*M+1):
  if i == 1:
    dp[1] = 0
  elif i == 2:
    dp[2] = 1
  elif i == 3:
    dp[3] = 2
  elif i%2 == 0:
    dp[i] = 1 + (dp[i//2] * 2)
  elif i%2 == 1:
    dp[i] = 1 + dp[i//2] + dp[i//2 + 1]

print(dp[-1])





