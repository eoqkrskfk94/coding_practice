import sys
sys.setrecursionlimit(100000)
Min = 1000000001
Max = -1000000001

N = int(sys.stdin.readline())

numbers = list(map(int,sys.stdin.readline().split()))

operators = list(map(int,sys.stdin.readline().split()))


def dfs(idx,result):
  global Max, Min
  if idx == N-1:
    Max = max(Max, result)
    Min = min(Min, result)
    return

  for i in range(4):
    if operators[i] != 0:
      operators[i] -= 1

      if i == 0:
        dfs(idx+1, result + numbers[idx+1])
      elif i == 1:
        dfs(idx+1, result - numbers[idx+1])
      elif i == 2:
        dfs(idx+1, result * numbers[idx+1])
      elif i == 3:
        dfs(idx+1, int(result / numbers[idx+1]))

      operators[i] += 1
      

dfs(0,numbers[0])

print(Max)
print(Min)



