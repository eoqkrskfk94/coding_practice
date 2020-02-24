import sys

N = int(sys.stdin.readline())

if N < 100:
  print(N)
elif N < 110:
  print(99)
else:
  total = 0
  for i in range(110,N+1,10):
    temp = list(str(i))
    gongcha = int(temp[1]) - int(temp[0])
    temp[2] = str(int(temp[1]) + gongcha)

    temp2 = "".join(temp)

    if int(temp[1]) + gongcha >= 0 and int(temp[1]) + gongcha < 10:
      temp2 = int("".join(temp))
      if temp2 <= N:
        total += 1


  
  print(total + 99)
    
