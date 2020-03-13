import sys

numbers = []
while True:
  N = list(map(int,sys.stdin.readline().split()))
  if N[0] == 0:
    break
  numbers.append(N[1:])

def dfs(num, idx1, idx2, lotto):
  if idx2 == 6:
    for i in range(6):
      print(lotto[i], end=" ")
    print()
    return

  for i in range(idx1, len(num)):
    lotto[idx2] = num[i]
    dfs(num, i+1, idx2+1, lotto)





for i in range(len(numbers)):
  lotto = [0] * 6
  dfs(numbers[i], 0,0, lotto)
  print()



