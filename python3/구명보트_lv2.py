################################################
# 스택을 사용한 풀이:
# 시간 초과: 스택을 사용해 pop을 이용시 시간이 더 걸림

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    while people:
        if(len(people) >= 2 and people[0] + people[-1] <= limit):
            people.pop(0)
            people.pop()
            answer += 1
        else:
            people.pop(0)
            answer += 1
                 
    return answer
    
################################################
    
################################################
# 순서를 사용한 풀이:
# 굳이 stack과 pop 없이 사용하면 더 간단하고 빠름

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start = 0
    end = len(people) -1
    #print(people)
    
    while start <= end:
        #print(start, end)
        if(start == end):
            answer += 1
            break
           
        elif(people[start] + people[end] <= limit):
            answer += 1
            start += 1
            end -= 1
               
        elif(people[start] + people[end] > limit):
            answer += 1
            start += 1

           
    return answer
    
################################################
