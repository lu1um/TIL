def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = [''] * cacheSize
    running_time = 0
    for city in cities:
        city = city.lower()
        for i in range(cacheSize):
            if city == cache[i]:
                running_time += 1
                cache.append(cache.pop(i))
                break
        else:   # LRU
            running_time += 5
            cache.pop(0)
            cache.append(city)
    return running_time
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))