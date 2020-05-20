import sys

board = []
answer = ""
longest = 0
for i in range(5):
    board.append(list(sys.stdin.readline().rstrip()))
    longest = max(longest, len(board[i]))

for i in range(longest):
    for j in range(5):
        if i < len(board[j]):
            answer += board[j][i]

print(answer)
