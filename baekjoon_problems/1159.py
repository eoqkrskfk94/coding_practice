import sys

N = int(sys.stdin.readline())
names = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()

    if name[0] in names:
        names[name[0]] += 1
    else:
        names[name[0]] = 1

answer = []
for name in names:
    if names[name] >= 5:
        answer.append(name)

if answer:
    print(''.join(sorted(answer)))
else:
    print('PREDAJA')
