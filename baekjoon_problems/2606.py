import sys
import collections

def bfs(current_node):
    queue = [current_node]
    visit = [current_node]

    while queue:
        current_node = queue.pop(0)

        for search_node in range(len(board[current_node])):
            if board[current_node][search_node] == 1 and search_node not in visit:
                board[current_node][search_node] = 0
                queue.append(search_node)
                visit.append(search_node)

    return visit

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

board = [[0] * N for i in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a-1][b-1] = 1
    board[b-1][a-1] = 1

answer = bfs(0)

print(len(answer)-1)
