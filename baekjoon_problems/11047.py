n, k = map(int, input().split())
coins = []
need = 0
for i in range(n):
    coins.append(int(input()))

for i in reversed(coins):
    temp = int(k/i)
    if temp > 0:
        k -= (temp*i)
        need += temp
    
print(need)
