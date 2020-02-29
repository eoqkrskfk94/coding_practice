import sys

N =int(sys.stdin.readline())

num = "666"
idx = 0
answer = 0

while idx < N:
  if "666" in num:
    idx += 1
    answer = int(num)
  
  temp = int(num) + 1
  num = str(temp)

print(answer)







    



