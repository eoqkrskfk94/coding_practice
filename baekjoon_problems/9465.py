import sys

N = int(sys.stdin.readline())

sticker = []
M = []
for i in range(N):
  temp = int(sys.stdin.readline())
  M.append(temp)
  line1 = list(map(int,sys.stdin.readline().split()))
  line2 = list(map(int,sys.stdin.readline().split()))
  sticker.append([line1, line2])


for i in range(N):
  dp = [[0] * M[i] for x in range(2)]
  dp[0][0] = sticker[i][0][0]
  dp[1][0] = sticker[i][1][0]
  for j in range(1,M[i]):
    if j == 1:
      dp[0][1] = sticker[i][1][0] + sticker[i][0][1]
      dp[1][1] = sticker[i][0][0] + sticker[i][1][1]
    else:
      dp[0][j] = max(sticker[i][0][j] + dp[1][j-1], sticker[i][0][j] + dp[1][j-2])
      dp[1][j] = max(sticker[i][1][j] + dp[0][j-1], sticker[i][1][j] + dp[0][j-2])


  print(max(max(dp[0]), max(dp[1])))



