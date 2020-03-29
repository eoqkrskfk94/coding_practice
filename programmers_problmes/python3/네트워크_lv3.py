def solution(n, computers):
    answer = 0
    visit = []
    for current_node in range(n):
        if current_node in visit:
            continue
        
        answer += 1
        queue = [current_node]
        visit += [current_node]
        
        while(queue):
            current_node = queue.pop(0)
            for search_node in range(n):
                if search_node not in visit and computers[current_node][search_node] == 1:
                    queue.append(search_node)
                    visit += [search_node]

    
    
    return answer
