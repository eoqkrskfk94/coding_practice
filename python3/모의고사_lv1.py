def solution(answers):
    answer = []
    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    
    for i, n in enumerate(answers):
        if n == A[i%5]:
            count[0] = count[0] + 1
        if n == B[i%8]:
            count[1] = count[1] + 1
        if n == C[i%10]:
            count[2] = count[2] + 1
    
    for i , score in enumerate(count):
        if score == max(count):
            answer.append(i+1)
        
    return answer
