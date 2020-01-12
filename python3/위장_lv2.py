################################################
# 리스트을 사용한 풀이:
# (옷 종류 갯수) * (옷 종류 갯수) * ... * (옷 종류 갯수) 
# 추가로 스파이는 한 종류의 옷만 입어도 되기 때문에 각각 1을 더해주면서 그 해당 옷을 입지 않은 상태를 더해준다
# (옷 종류 갯수 + 1) * (옷 종류 갯수 + 1) * ... * (옷 종류 갯수 + 1)
# 또한 스파이는 무조건 최소 한개의 옷을 착용해야하므로 아무것도 착용하지 않은 상태를 빼줘야한다.
# (옷 종류 갯수 + 1) * (옷 종류 갯수 + 1) * ... * (옷 종류 갯수 + 1) - 1

def solution(clothes):
    answer = 1
    kind = []
    count = []

    for x, y in clothes:
        if y not in kind:
            kind.append(y)
            count.append(1)
            continue
        if y in kind:
            count[kind.index(y)] += 1
            
    for number in count:
        answer *= (number + 1)
        print(number)
    
    #print(count)
    #print(answer)
        
    return answer - 1
