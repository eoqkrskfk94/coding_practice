N = input()

if '0' not in N:
    print(-1)
else:
    N = list(map(int,N))
    N.sort(reverse = True)

    if sum(N)%3 != 0:
        print(-1)
    else:
        answer =""
        for i in range(len(N)):
            answer += str(N[i])
        print(int(answer))
