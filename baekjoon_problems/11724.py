import sys
sys.setrecursionlimit(100000)
N, K = map(int,sys.stdin.readline().split())

tree = [[0] * N for i in range(N)]

for i in range(K):
  x, y = map(int,sys.stdin.readline().split())
  tree[x-1][y-1] = 1
  tree[y-1][x-1] = 1

def dfs(current_node,tree,visited):
  visited += [current_node]

  for search_node in range(len(tree[current_node])):
    if tree[current_node][search_node] == 1 and search_node not in visited:
      visited = dfs(search_node,tree,visited)
  
  return visited

def bfs(start, tree):
  queue = [start]
  visited = [start]

  while(queue):
    current_node = queue.pop(0)
    for search_node in range(len(tree[current_node])):
      if tree[current_node][search_node] == 1 and search_node not in visited:
        visited += [search_node]
        queue += [search_node]

  return visited


connected = [bfs(0,tree)]
#connected =  [dfs(0,tree,[])]

for i in range(1,N):
  flag = 1
  for j in range(len(connected)):
    if i in connected[j]:
      flag = 0
      break
  if flag == 1:
    #temp = dfs(i,tree,[])
    temp = bfs(i,tree)
    connected.append(temp)

#print(connected)
print(len(connected))






