# 힙을 사용하여 stock이 다 떨어지지 않은 날짜까지에서 제일 크게 supply를 받을 수 있는 날짜에서 받는다. 
# 힙은 자동으로 정렬을 해주기때문에 사용하기 편하다. 

import heapq

def solution(stock, dates, supplies, k):
    idx = 0
    answer = 0
    heap = []
    while stock < k:
        for i in range(idx , len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap, (-supplies[i], supplies[i]))
                #heap.append(supplies[i])
                idx += 1
            else:
                break
        

        stock += heapq.heappop(heap)[1]
        #stock += max(heap)
        answer += 1

    
    return answer
