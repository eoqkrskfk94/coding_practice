# 매번 각 행의 최댓값을 구하고 그 열을 제외하고 최댓값을 구하는건 시간 낭비이다. (시간초과)
# 풀이: 
# 각 위치에서 전 행의 같은 열을 제외하여 각각 더해서 그중에서 최댓값을 구하고 해당 땅의 점수를 그 최대값으로 바꿔준다.
# 그리고 마지막 행에서 최댓값을 return 해주면된다.

def solution(land):
    answer = 0  
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
        
    answer = max(land[-1])
    return answer
