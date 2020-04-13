import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

temp = str(A*B*C)

hip = [0] * 10
for num in temp:
  hip[int(num)] += 1

for i in range(10):
  print(hip[i])







