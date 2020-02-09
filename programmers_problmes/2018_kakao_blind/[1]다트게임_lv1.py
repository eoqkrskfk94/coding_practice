# 풀이:
# 조건부 

def solution(dartResult):
    score = []
    idx = 0
    temp = 0
    n = 0
    length = len(dartResult) - 1
    while n < length:
        if dartResult[n] == '1' and dartResult[n+1] == '0':
            num = 10
            n += 1
        else:
            num = int(dartResult[n])
          
        if dartResult[n+1] == 'S':
            score.append(num)
        elif dartResult[n+1] == 'D':
            score.append(num ** 2)
        elif dartResult[n+1] == 'T':
            score.append(num ** 3)
        
        if n+2 <= length and dartResult[n+2] == '#':
            score[-1] *= -1
        elif n+2 <= length and dartResult[n+2] == '*':
            score[-1] *= 2
            if score[-1] != score[0]:
                score[-2] *= 2
        
        if n + 2 <= length and (dartResult[n+2] == '*' or dartResult[n+2] == '#'):
            n += 3
        else:
            n += 2
        
        
    return sum(score)
