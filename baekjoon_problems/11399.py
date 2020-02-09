people = int(input())
timetable = list(map(int, input().split()))

timetable.sort()
time = 0
total = 0
    
for i in range(people):
    time += timetable[i]
    total += time

print(total)
