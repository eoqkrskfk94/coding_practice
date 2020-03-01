import sys

N, M, V = map(int, sys.stdin.readline().split())

tree = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
  temp = list(map(int, sys.stdin.readline().split()))
  tree[temp[0]][temp[1]] = 1
  tree[temp[1]][temp[0]] = 1

def dfs(current_node, row, visits):
  visits += [current_node]
  for search_node in range(len(row[current_node])):
    if row[current_node][search_node] and search_node not in visits:
      visits = dfs(search_node, row, visits)
  return visits

def bfs(start):
  queue = [start]
  visits = [start]
  while queue:
    current_node = queue.pop(0)
    for search_node in range(len(tree[current_node])):
      if tree[current_node][search_node] and search_node not in visits:
        visits += [search_node]
        queue += [search_node]
  
  return visits


  


df = (dfs(V,tree,[]))
bf = (bfs(V))

for node in df:
  print(node, end = " ")
print()
for node in bf:
  print(node, end = " ")
    


