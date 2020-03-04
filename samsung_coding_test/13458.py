import sys

N = int(sys.stdin.readline())

rooms = list(map(int,sys.stdin.readline().split()))

B, C = map(int,sys.stdin.readline().split())

total = 0
for room in rooms:
  room -= B
  total += 1
  if room <= 0:
    continue

  if room % C == 0:
    total += (room//C)
  else:
    total += (room//C)
    total += 1

print(total)




