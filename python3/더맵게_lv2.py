################################################
# 스택을 사용한 풀이:
# 시간 초과: 매번 섞은 음식을 다시 리스트에 넣고 sort하여 시간이 오래걸림

def solution(scoville, K):
    answer = -1
    mix_count = 0
    scoville.sort(reverse = True)
    
    while min(scoville) < K:
        try:
            scoville.append(scoville.pop() + (scoville.pop() * 2))
        except IndexError:
            return -1
        mix_count += 1
        scoville.sort(reverse = True)
        
    answer = mix_count
    return answer
################################################
    
################################################
# 힙을 사용한 풀이:
# 힙은 일반적인 리스트와 다르게, 가지는 요소를 pop이나 push를 할때마다 자동으로 정렬해준다.

import heapq

def solution(scoville, K):
    answer = -1
    mix_count = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    
    while heap[0] < K:
        try:
            heapq.heappush(heap, (heapq.heappop(heap) + heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_count += 1
        
    answer = mix_count
    return answer
    
################################################
