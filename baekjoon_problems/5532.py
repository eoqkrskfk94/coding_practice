import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

korean = A//C
if A%C != 0:
    korean += 1
math = B//D
if B%D != 0:
    math += 1


if korean >= math:
    print(L - korean)
else:
    print(L - math)
