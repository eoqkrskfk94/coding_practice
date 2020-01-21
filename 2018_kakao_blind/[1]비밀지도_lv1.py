# 풀이:
# zip를 사용하여 2개의 지도의 가로 배열을 짝을 지어준다
# 각각 짝들을 2진수로 만들때 한 지도라도 1이 나오면 해당 지역은 벽이고 둘다 1이 안나오면 벽이 없는것이다.
# 마지막으로 구한 한 가로의 지도를 이어붙여 return 해준다

def solution(n, arr1, arr2):
    answer = []
    for x,y in zip(arr1, arr2):
        temp =[0] * n
        wall = ""
        for i in reversed(range(n)):
            if x % 2 == 0:
                x = x/2
            else:
                temp[i] = 1
                x = (x-1)/2
                
            if y % 2 == 0:
                y = y/2
            else:
                temp[i] = 1
                y = (y-1)/2
                
            if temp[i] == 1:
                wall = "#" + wall
            else:
                wall = " " + wall
        answer.append(wall)
            
    return answer
