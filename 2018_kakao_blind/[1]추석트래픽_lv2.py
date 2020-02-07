# 풀이:
# 윈도우 형식의 모든 순간을 for으로 반복문을 돌려 각각 겹치는 처리량을 찾기에는 너무나 많은 시간이 소유된다. 
# 하지만 문제를 잘 분석하면 요청의 변화는 해당 요청의 시각과 끝 뿐이다. 그렇기 때문에 모든 요청의 시각과 끝을 구하고 
# 그 시가과 끝에서 1초 거리에 있는 모든 처리량을 계산하여 최대로 처리량이 많은 값을 return 해주면된다.
# time complexity : O(n^2)

import datetime
def solution(lines):
    answer = 0
    max = 0
    starts = []
    ends = []    
    
    if len(lines) == 1:
        return 1
    
    for line in lines:
        date, time, duration = line.split()
        hour, min, nano = time.split(':')
        hour = int(hour) * 1000
        min = int(min) * 1000  
        sec = int(nano[0:2] + nano[3:])
        end = hour * 60 * 60 + min * 60 + sec
        duration = duration.replace("s","")
        duration = duration.split('.')

        if len(duration)>1:
             duration = int(duration[0])*1000 + int(duration[1]+('0'*(3-len(duration[1]))))
        else: duration = int(duration[0])*1000
        
        start = end - duration + 1
        starts.append(start)
        ends.append(end)
    
    temp = zip(starts, ends)
    temp = sorted(temp)
        
    for i in range(len(temp)):
        count = 1
        new_end = temp[i][1]
        for j in range(len(temp)):
            if i != j:
                if temp[j][0] < new_end + 1000 and temp[j][1] > new_end:
                    count += 1
        count2 = 1   
        new_end = temp[i][0]
        for j in range(len(temp)):
            if i != j:
                if temp[j][0] < new_end + 1000 and temp[j][1] > new_end:
                    count2 += 1
                    
        if count > count2:
            max = count
        else:
            max = count2
            
        if max > answer:
            answer = max

    

    return answer
