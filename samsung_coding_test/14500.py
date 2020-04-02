import sys
blocks = [["1111",
           "0000",
           "0000",
           "0000"],

          ["1000",
           "1000",
           "1000",
           "1000"],

          ["1100",
           "1100",
           "0000",
           "0000"],    

          ["1000",
           "1000",
           "1100",
           "0000"],       

          ["0100",
           "0100",
           "1100",
           "0000"],  

          ["1110",
           "1000",
           "0000",
           "0000"],  

          ["1000",
           "1110",
           "0000",
           "0000"],  
          
          ["1100",
           "0100",
           "0100",
           "0000"], 

          ["1100",
           "1000",
           "1000",
           "0000"],   
          
          ["0010",
           "1110",
           "0000",
           "0000"],  

          ["1110",
           "0010",
           "0000",
           "0000"],

          ["1000",
           "1100",
           "0100",
           "0000"],  

          ["0100",
           "1100",
           "1000",
           "0000"],    

          ["0110",
           "1100",
           "0000",
           "0000"],

          ["1100",
           "0110",
           "0000",
           "0000"],  

          ["1110",
           "0100",
           "0000",
           "0000"], 

          ["0100",
           "1100",
           "0100",
           "0000"],

          ["0100",
           "1110",
           "0000",
           "0000"],   

          ["1000",
           "1100",
           "1000",
           "0000"],   
          ]

def count(y,x,block):
  total = 0
  for i in range(4):
    for j in range(4):
      if block[i][j] == '1':
        total += board[y+i][x+j]
  
  return total


N, M = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
  temp = list(map(int,sys.stdin.readline().split()))
  temp += [-10000,-10000,-10000]
  board.append(temp)

temp = [-10000] * (M+3)
for i in range(3):
  board.append(temp)


answer = 0

for block in blocks:
  for i in range(N):
    for j in range(M):
      total = count(i,j,block)
      answer = max(answer,total)

print(answer)

