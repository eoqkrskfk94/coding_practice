import copy

def solution(phone_book):
    answer = True
    
    for idx, number in enumerate(phone_book):
        check = copy.deepcopy(phone_book)
        check.pop(idx)
        
        for i in check:
            if number == i[:len(number)]:
                return False

    return answer
