import sys

N = int(sys.stdin.readline())
answer = 0

bag5 = 0
bag3 = 0

while N > 0:
  if 1 <= N < 3 or N == 4:
    answer = -1
    break

  if (N - 5)% 5 == 0 or (N-5) % 3 == 0:
    answer += 1
    N -= 5
  
  else:
    answer += 1
    N -= 3


print(answer)




