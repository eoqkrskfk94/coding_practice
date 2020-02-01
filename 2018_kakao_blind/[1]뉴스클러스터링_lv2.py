# 풀이:
# 문자열 짝을 만들어준다
# 교집합과 합집합을 만들어 각각 몇개씩 나오는지 확인하여 교집합은 최솟값을 합집합은 최댓값을 찾아 각각 구해준다. 

def solution(str1, str2):
    str_arr1 = []
    str_arr2 = []
    str1, str2 = str1.lower(), str2.lower()
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str_arr1.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str_arr2.append(str2[i] + str2[i+1])
        
    
    inter = set(str_arr1) & set(str_arr2)
    union = set(str_arr1) | set(str_arr2)
    
    if len(union) == 0:
        return 65536
    
    inter_n = sum([min(str_arr1.count(i), str_arr2.count(i)) for i in inter])
    total = sum([max(str_arr1.count(i), str_arr2.count(i)) for i in union])
    
    
    return int(65536 * (inter_n/(total)))
 
