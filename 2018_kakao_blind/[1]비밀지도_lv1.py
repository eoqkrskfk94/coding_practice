def solution(n, arr1, arr2):
    answer = []
    for x,y in zip(arr1, arr2):
        temp =[0] * n
        wall = ""
        for i in reversed(range(n)):
            if x % 2 == 0:
                x = x/2
            else:
                temp[i] = 1
                x = (x-1)/2
                
            if y % 2 == 0:
                y = y/2
            else:
                temp[i] = 1
                y = (y-1)/2
                
            if temp[i] == 1:
                wall = "#" + wall
            else:
                wall = " " + wall
        answer.append(wall)
            
    return answer
