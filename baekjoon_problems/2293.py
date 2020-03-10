import sys

N, M= map(int,sys.stdin.readline().split())

coins = []
coins.append(0)
for i in range(N):
  coins.append(int(sys.stdin.readline()))

#print(coins)

dp = [0] * (M+1)

for i in range(1,N+1):
  for j in range(1,M+1):
    temp = j - coins[i]
    if coins[0] == i and coins[0] <= j:
      dp[j] = 1
    elif coins[i] == j:
      dp[j] += 1
    elif coins[i] < j:
      dp[j] += dp[temp]
      
  
print(dp[-1])






