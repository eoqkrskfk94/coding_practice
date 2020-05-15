import sys

def prime(number):
    count = 0
    flag = 1
    if number < 2:
        return 0

    if number < 4:
        return 1

    if number % 2 == 0:
        return 0

    if number % 3 == 0:
        return 0

    l = round(number ** 0.5) + 1
    for i in range(3,l, 2):
        if(number % i == 0):
            return 0

    return 1

answer = []
while True:
    count = 0
    N = int(sys.stdin.readline())
    if N == 0:
        break


    for i in range(N+1,2*N+1):
        if prime(i):
            count += 1

    answer.append(count)

for ans in answer:
    print(ans)
