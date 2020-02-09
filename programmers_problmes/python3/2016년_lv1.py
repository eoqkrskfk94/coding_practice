def solution(a, b):
    answer = ''
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    cal = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    total = 0

    for i in range(a):
        total+= cal[i]
        
    total += (b-1)
    
    temp = days[total%7]
    print(temp)
    answer = temp
    return answer
