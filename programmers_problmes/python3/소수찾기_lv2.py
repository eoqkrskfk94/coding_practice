from itertools import permutations

def prime(number):
    if number == 1 or number == 0:
        return -1
    for i in range(2,number-1):
        if number % i == 0:
            return -1
    
    return 1

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num_list = []
    for i in range(1,len(numbers)+1):
        perm = permutations(numbers,i)
        for j in perm:
            num = (int("".join(list(j))))
            if num not in num_list and prime(num) == 1:
                num_list.append(num)
                answer += 1
    
    return answer
