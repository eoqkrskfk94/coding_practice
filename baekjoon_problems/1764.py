import sys

N, M = map(int,sys.stdin.readline().split())

answer = []
names = []
for i in range(N+M):
  name = sys.stdin.readline().rstrip()
  names.append(name)

names.sort()
#print(names)


idx = 0
while True:
  if idx == len(names) -1:
    break
  
  #print(names[idx])

  if names[idx] == names[idx+1]:
    if not answer:
      answer.append(names[idx])
    elif answer[-1] != names[idx]:
      answer.append(names[idx])
  
  idx += 1



#print()


print(len(answer))
for i in range(len(answer)):
  print(answer[i])





