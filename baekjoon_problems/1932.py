import sys

N = int(sys.stdin.readline())

tri = []
for i in range(N):
  tri.append(list(map(int,sys.stdin.readline().split())))

tri = tri[::-1]

#print(tri)

for i in range(1,N):
  for j in range(len(tri[i])):
    tri[i][j] = max(tri[i][j] + tri[i-1][j], tri[i][j] + tri[i-1][j+1])


print(tri[-1][0])


