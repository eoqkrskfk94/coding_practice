################################################
# 리스트에서 확인후 삭제하는 풀이:
# 시간 초과: 모든 선수를 봐야한다

def solution(participant, completion):
    answer = ''
    for part in completion:
        if part in participant:
            participant.remove(part)
            
    print(participant)
    answer = participant[0]
    return answer
    
################################################
    
################################################
# zip을 사용한 풀이: 
# 짝을 만들어 그 짝이 같이 않을때 확인

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for x,y in zip(participant, completion):
        if x != y:
            return x
    
    return participant[-1]
    
################################################
