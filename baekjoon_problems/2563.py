import sys

N = int(sys.stdin.readline())
papers = []
board = [[0] * 100 for i in range(100)]
count = 0
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            if board[i][j] == 0:
                board[i][j] = 1
                count+= 1

print(count)
