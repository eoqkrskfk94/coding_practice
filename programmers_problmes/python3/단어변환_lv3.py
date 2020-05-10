answer = 1000000

def check(word1, word2):
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
            
    if diff == 1:
        return 1
    else:
        return 0
            
            
def dfs(word, words, target, count, visit):
    global answer
    if word == target:
        answer = min(answer, count)
        return
    
    if len(visit) == len(words):
        return
    
    for i in range(len(words)):
        if check(word, words[i]) and words[i] not in visit:
            visit.append(words[i])
            dfs(words[i], words, target, count+1, visit)
            visit.pop()
    
    

def solution(begin, target, words):
    global answer
    
    if target not in words:
        return 0
    
    dfs(begin, words, target, 0, [])

    return answer