def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    num = len(citations)
    
    if min(citations) >= num:
        return num
    
    left = 0
    right = len(citations) - 1
    print(citations)
    for i,n in enumerate(citations):
        if n <= i:
            return i
    
    return 0
   
    print(answer)
    return answer
