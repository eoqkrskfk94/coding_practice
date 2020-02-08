# Greedy 문제:
# stack를 이용한다
# stack에서 마지막 스택보다 작은 수가 들어오면 넣어준다. 큰 수가 들어오면 앞에 있는 수와 비교하여 작은 수는 다 빼준다 (k 만큼만 빼준다)
# k 가 0이되면 나머지는 다 이어붙혀준다

def solution(number, k):
    answer = ''
    stack = []
    for idx in range(len(number)):
        if not stack:
            stack.append(number[idx])
        elif stack[-1] >= number[idx]:
            stack.append(number[idx])
        elif k > 0 and stack[-1] < number[idx]:
            for i in reversed(stack):
                if i < number[idx] and k > 0:
                    stack.pop()
                    k -= 1
                else:
                    break
            stack.append(number[idx])
        elif k == 0: 
            stack.append(number[idx])
            
        idx += 1
    if k == 0:
        answer = "".join(stack)
    else:
        answer = "".join(stack[:-k])
    return answer
