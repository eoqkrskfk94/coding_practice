import sys

N = int(sys.stdin.readline())

wine = []
for i in range(N):
  wine.append(int(sys.stdin.readline()))

max_amt = [0] * N

if N == 1:
  print(wine[0])
elif N == 2:
  print(wine[1] + wine[0])
elif N >= 3:

  max_amt[0] = (wine[0])
  max_amt[1] = (wine[0] + wine[1])
  max_amt[2] = (max(wine[2] + wine[1], wine[2] + wine[0]))
  max_amt[2] = max(max_amt[2], max_amt[1])

  if N == 3:
    print(max(max_amt))
  
  if N > 3:
    for i in range(3,N):
      max_amt[i] = (max(wine[i] + wine[i-1] + max_amt[i -3], wine[i] + max_amt[i-2]))
      max_amt[i] = max(max_amt[i], max_amt[i-1])

    print(max(max_amt))





