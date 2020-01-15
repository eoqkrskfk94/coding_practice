def solution(heights):
    answer = []
    for i in range(len(heights)):
        answer.append(0)
    print(heights)
    for tower, height in enumerate(heights):
        count = tower
        while count >= 0:
            if heights[count] > height:
                answer[tower] = count+1
                count -= 1
                break
            count -= 1
    return answer
