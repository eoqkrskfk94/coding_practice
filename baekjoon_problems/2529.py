import sys


N = int(sys.stdin.readline())
signs = sys.stdin.readline().split()
numbers = [True] * 10
maxim, minim = 0, 9999999999


def possible(i, j, k):
  if k == '>':
    return i > j
  if k == '<':
    return i < j
  return True

def solve(num, idx):
  
  global maxim, minim
  if idx == N+1:
    if int(num) > int(maxim):
      maxim = num
    if int(num) < int(minim):
      minim = num
    return

  for i in range(10):
    if numbers[i]:
      if idx == 0 or possible(num[-1], str(i), signs[idx-1]):
        numbers[i] = False
        solve(num+str(i), idx+1)
        numbers[i] = True


solve("", 0)
print(maxim)
print(minim)
