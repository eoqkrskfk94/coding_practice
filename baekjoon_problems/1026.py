import sys

N = int(sys.stdin.readline())

arr1 = list(map(int,sys.stdin.readline().split()))
arr2 = list(map(int,sys.stdin.readline().split()))

arr1.sort(reverse = True)
arr2.sort()

total = 0
for i in range(N):
  total += (arr1[i] * arr2[i])

print(total)
