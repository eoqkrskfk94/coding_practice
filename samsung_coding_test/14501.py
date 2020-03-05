import sys

N = int(sys.stdin.readline())

date = []
max_pay = [-1] * N

for i in range(N):
  T, P = map(int,sys.stdin.readline().split())
  date.append([T,P])

def solve(day):

  if day > N:
    return -999999
  if day == N:
    return 0

  total = max_pay[day]
  if total != -1:
    return total
  
  total = max(solve(day+1), solve(day + date[day][0]) + date[day][1] )

  max_pay[day] = total

  return total





total = solve(0)
#print(max_pay)
print(total)

