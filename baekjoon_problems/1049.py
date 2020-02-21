import sys
N, M = map(int,sys.stdin.readline().split())

brands = []
brands_string = []
for i in range(M):
  temp = list(map(int,sys.stdin.readline().split()))
  brands.append(temp)
  brands_string.append(temp)

brands.sort()
brands_string.sort(key = lambda x: (x[1], x[0]))
#print(brands)
#print(brands_string)

cost1, cost2 = brands[0][0], brands_string[0][1]

if N <= 6:
  if cost1 < cost2 * N:
    print(cost1)
  else:
    print(cost2*N)
else:
  if N%6 == 0:
    new_cost1 = cost1* (N//6)
  else:
    new_cost1 = cost1* (N//6 + 1)
  
  new_cost2 = cost2 * N
  new_cost3 = cost1 * (N//6) + cost2 * (N%6)

  print(min(new_cost1,new_cost2,new_cost3))
