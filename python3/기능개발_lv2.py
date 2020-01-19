################################################
# 스택을 사용한 풀이:
# 시간 문제: 시간 복잡도 O(n^2)

def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
                
        count = 0
        while True:
            if progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                if count > 0:
                    answer.append(count)
                break
                
    return answer
    
################################################
    
################################################
# 100%까지 얼마나 걸리는지 미리 저정한 리스트를 사용한 풀이:
# 시간 복잡도: O(n)

import math
def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    print(progresses)

    temp = 0
    count = 0
    for i in range(len(progresses)):
        print(progresses[temp],progresses[i])
        
        if progresses[temp] < progresses[i]:
            answer.append(count)
            count = 1
            temp = i
        else:
            count+= 1

    answer.append(count)
    return answer
    
################################################
