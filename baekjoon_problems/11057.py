import sys

N = int(sys.stdin.readline())

dp = [0] * 10

for i in range(N):
  for j in range(10):
    if i == 0:
      dp[j] = j+1
    elif j == 0:
      dp[j] = 1
    else:
      dp[j] = dp[j-1] + dp[j]
  
print(dp[-1]%10007)


