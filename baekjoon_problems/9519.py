import sys
import copy

N = int(sys.stdin.readline())
word = list(sys.stdin.readline().rstrip())

M = len(word)//2
pattern = [word[:]]

for i in range(N):
    last = []
    idx = 1
    for j in range(M):
        last.append(word[1 + j])
        del word[1 + j]

    word = word + last[::-1]


    if word == pattern[0]:
        break

    pattern.append(word[:])



print("".join(pattern[N%len(pattern)]))
