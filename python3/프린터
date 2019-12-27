
def solution(priorities, location):
    answer = 0
    printer = []
    count = 0
    for i in range(len(priorities)):
        printer.append(i)
    
    m = max(priorities)
    while True:
        if(priorities[0] < m):
            priorities.append(priorities.pop(0))
            printer.append(printer.pop(0))
        else:
            count += 1
            priorities.pop(0)
            if printer.pop(0) == location:
                return count
            m = max(priorities)
                
                
    print(priorities)
    print(printer)
    return answer
