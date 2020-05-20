import sys

students = [0] * 30

for i in range(28):
    students[int(sys.stdin.readline())-1] = 1

answer = []
for i in range(30):
    if students[i] == 0:
        answer.append(i+1)



print(answer[0])
print(answer[1])
