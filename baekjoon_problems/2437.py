N = int(input())
weights = list(map(int,input().split(" ")))

weights.sort()
#print(weights)
if weights[0] != 1:
  print(1)

else:
  total = 1
  for i in range(1,N):
    if total + 2 <= weights[i]:
      break
    
    total += weights[i]
  
  print(total + 1)
  
  



  

