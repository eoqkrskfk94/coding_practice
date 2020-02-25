import sys

N = int(sys.stdin.readline())

words = []
for i in range(N):
  words.append(sys.stdin.readline().rstrip())

count = 0
for word in words:
  alpha = []
  alpha.append(word[0])
  group = True
  for i in range(1,len(word)):
    if word[i] not in alpha:
      alpha.append(word[i])
    elif word[i] == word[i-1]:
      continue
    else:
      group = False
      break
  
  if group == True:
    count += 1

print(count)
    



