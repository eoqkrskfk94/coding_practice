def bfs(current_node, computers, n):
    answer = 0
    visit = []
    
    for current_node in range(n):
        if current_node in visit:
            continue
        
        answer += 1
        
        queue = [current_node]
        visit += [current_node]
    
        while queue:
            current_node = queue.pop(0)
            for search_node in range(n):
                if computers[current_node][search_node] == 1 and search_node not in visit:
                    queue.append(search_node)
                    visit.append(search_node)
                    
    return answer

        
        
def solution(n, computers):
    answer = bfs(0, computers, n)
    return answer
