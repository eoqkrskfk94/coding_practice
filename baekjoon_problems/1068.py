def find(x, tree):
  global count

  if len(tree[x]) == 0:
    count += 1
  else:
    for i in tree[x]:
      find(i, tree)

count = 0

n = int(input())

l = list(map(int,input().split()))

tree = [[] for i in range (50)]

for i in range(len(l)):
  if l[i] == -1:
    start = i
  else:
    tree[l[i]].append(i)

m = int(input())

for i in range(n):
  if m in tree[i]:
    tree[i].remove(m)

if m != start:
  find(start , tree)


#print(tree)
print(count)




