import sys
T = int(sys.stdin.readline())
total_group = []
for t in range(T):
  grade = []
  N = int(sys.stdin.readline())
  for i in range(N):
    grade.append(list(map(int,sys.stdin.readline().split())))
  
  grade.sort()

  drop = 0
  cutline = grade[0][1]
  for i in range(1,len(grade)):
    if grade[i][1] > cutline:
      drop += 1
    else:
      cutline = grade[i][1]
  print(len(grade) - drop)
