import sys

N, M = map(int, input().split())

answer = []

for i in range(M, 101):
  end = (N//i + i//2)
  start = (end - i + 1)

  if start < 0:
    break

  e = (end * (end + 1))
  s = ((start - 1) * (start))


  if e - s == N*2:
    answer.append(start)
    answer.append(end)
    break

if len(answer) == 0 or answer[1] - answer[0] + 1 > 100:
  print(-1)

else:
  for i in range(answer[0],answer[1] + 1):
    print(i, end = " ")


    
