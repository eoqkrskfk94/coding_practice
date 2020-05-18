import sys
answer = []
while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0 and C == 0:
        break

    if (C*C + B*B) == A*A:
        answer.append('right')

    elif (A*A + C*C) == B*B:
        answer.append('right')

    elif (A*A + B*B) == C*C:
        answer.append('right')
        
    else:
        answer.append('wrong')


if answer:
    for i in range(len(answer)):
        print(answer[i])
