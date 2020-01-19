# Greedy 문제로 
# 첫째: letter를 변경할때 조이스틱을 위로 조절하거나 아래로 조절했을때의 이동 크기를 비교해 작은 쪽을 선택
# 둘째: 이동을 할때 다음 구간이 A가 아닐때의 걸리는 이동 횟수 (왼쪽으로 이동, 오른쪽으로 이동)를 비교해 작언 쪽을 선택

def solution(name):
    answer = 0
    name = list(name)
    letter = 0
    result = ['A'] * len(name)

    
    while (True):
        left = 1
        right = 1
        if name[letter] != 'A':
            if ord(name[letter]) - ord('A') < 14:
                answer += (ord(name[letter]) - ord('A'))
                name[letter] = 'A'
            else:
                answer += (90 - ord(name[letter]) + 1)
                name[letter] = 'A'
                
            if name == result:
                break
        else:
            for i in range(1, len(name)):
                if name[letter + i] == 'A':
                    right += 1
                else:
                    break
                
                if name[letter - i] == 'A':
                    left += 1
                else:
                    break
            if right > left:
                answer += left
                letter -= left
            else:
                answer += right
                letter += right
                
    print(result)
    return answer
