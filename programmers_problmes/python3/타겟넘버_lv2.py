# 풀이:
# recursive function을 사용하여 DFS 트리를 구현. 트리의 자식은 더하기 빼기만 있기 때문에 
# 모든 조합을 검색해 값을 구한다.

def solution(numbers, target):
    cnt = 0
    
    def function(numbers, target, idx):
        if idx < len(numbers):
            
            numbers[idx] *= 1
            function(numbers, target, idx+1)

            numbers[idx] *= -1
            function(numbers, target, idx+1)
            

        else:
            if sum(numbers) == target:
                nonlocal cnt
                cnt += 1

    function(numbers, target, 0)

    return cnt




# 다른 방법




answer = 0

def dfs(numbers, idx, target):
    global answer

    if idx == len(numbers):

        if sum(numbers) == target:
            answer += 1
        return
    
    dfs(numbers, idx+1, target)
    numbers[idx] *= -1
    dfs(numbers, idx+1, target)
    
    
    
        
def solution(numbers, target):
    
    dfs(numbers,0, target)
    return answer
