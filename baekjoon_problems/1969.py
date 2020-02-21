N, M = map(int,input().split())

dna = []
answer = ''
diff = 0

for i in range(N):
  dna.append(input())


for i in range(M):
  count = [0,0,0,0]
  for j in range(N):
    if dna[j][i] == 'A':
      count[0] += 1
    elif dna[j][i] == 'C':
      count[1] += 1
    elif dna[j][i] == 'G':
      count[2] += 1
    elif dna[j][i] == 'T':
      count[3] += 1
  
  Max = max(count)
  diff += (int(N)- Max)
  temp = count.index(Max)
  if temp == 0:
    answer += 'A'
  elif temp == 1:
    answer += 'C'
  elif temp == 2:
    answer += 'G'
  elif temp == 3:
    answer += 'T'


print(answer)
print(diff)
