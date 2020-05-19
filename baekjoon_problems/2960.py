import sys

N, K = map(int,sys.stdin.readline().split())

numbers = [x for x in range(2,N+1)]
deletes = []

while numbers:

  prime = numbers[0]
  temp = []
  for j in range(len(numbers)):
    if numbers[j] % prime != 0:
      temp += [numbers[j]]
    else:
      deletes += [numbers[j]]
  
  numbers = temp

print(deletes[K-1])


