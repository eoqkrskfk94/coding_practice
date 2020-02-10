
change = [500,100,50,10,5,1]
n = 1000 - int(input())
answer = 0

for i in range(len(change)):
    temp = int(n/change[i])
    if temp > 0:
        answer += temp
        n -= (temp * change[i])
        
print(answer)
