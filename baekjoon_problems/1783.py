import sys

N, M = sys.stdin.readline().split()
N, M = int(N), int(M)

if N == 0 or M == 0:
  print(0)

elif N == 1 or M == 1:
  print(1)

elif N == 2:
  if M <= 2:
    print(1)
  elif M == 3 or M == 4:
    print(2)
  elif M == 5 or M == 6:
    print(3)
  else:
    print(4)

elif M <= 4:
  print(M)

elif M == 5 or M == 6:
  print(4)

# N > 2, M > 6
else:
  print(M-2)













  



