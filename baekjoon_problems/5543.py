import sys

menu = [0,0,0,0,0]
for i in range(5):
    menu[i] = int(sys.stdin.readline())

min_burger = 2000
min_drink = 2000
for i in range(3):
    min_burger = min(min_burger, menu[i])


min_drink = min(menu[3], menu[4])

answer = min_drink + min_burger - 50

print(answer)
