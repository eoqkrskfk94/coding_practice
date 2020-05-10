def dfs(current, tickets, visit, answer):
    
    answer.append(current)
    
    for i in range(len(tickets)):
        if tickets[i][0] == current and tickets[i] not in visit:
            visit.append(tickets[i])
            visit,answer = dfs(tickets[i][1], tickets,visit,answer)
    
    return visit,answer
            

def solution(tickets):
    answer = []
    
    tickets.sort(key = lambda x : x[1])

    visit = []
    start = ''
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visit.append(tickets[i])
            start = tickets[i][1]
            break
    
           
    answer.append('ICN')

    visit, answer = dfs(start, tickets, visit, answer)

    return answer