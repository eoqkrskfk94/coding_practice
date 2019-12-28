def solution(arrangement):
    answer = 0
    stack = []
    for i in arrangement:
        stack.append(i)

    stick = 0
    laser = 0
    count = 0
    cut = 0
    
    while stack:
        temp = stack.pop()
        #print("stick: ", stick)
        if(temp == ')' and stack[-1] != '('):
            stick += 1
   
        elif(temp == ')' and stack[-1] == '('):
            laser += 1
            count += stick
            stack.pop()
            cut = 1
            
        elif(temp == '('):
            stick-= 1
            if(cut == 1):
                count += 1
            if(stick == 0):
                cut = 0
            
          

    #print(stick)
    print(count)
    answer = count
    return answer
