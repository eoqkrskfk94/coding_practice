# 풀이:
# 매번 캐시에 없는 새로운 도시가 나올때 캐시에 넣어준다. 만약 캐시 가 꽉차면 제일 캐시 리스트에 있는 첫번째 도시를 지우고 캐시 뒤에 추가주고 5초를 더해준다.
# 만약 도시에 캐시에 존재하면 해당 도시를 캐시 리스트에 제일 뒤로 옮겨준다 (캐시의 방식) 그리고 1초를 더해준다. (FIFO 방식)

def solution(cacheSize, cities):
    time = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            #print(cache.index(city))
            cache.pop(cache.index(city))
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
            time += 5
    return time
