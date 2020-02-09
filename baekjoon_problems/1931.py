N = int(input())
timetable = []
timetaken = []
totaltime = []
answer = 0


for i in range(N):
    st , en = map(int, input().split())
    timetable.append((st,en))
    timetaken.append(en - st)
 
timetable.sort(key = lambda x: (x[1], x[0]))

#print(timetable)

end = 0
for i in range(N):
  if timetable[i][0] >= end:
    end = timetable[i][1]
    answer += 1


#print(totaltime)
print(answer)
 



