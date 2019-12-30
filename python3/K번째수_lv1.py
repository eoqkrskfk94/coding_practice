def solution(array, commands):
    answer = []
    for i in commands:
        temp = []
        temp = sorted(array[i[0]-1:i[1]])
        answer.append(temp[i[2]-1])
    return answer
