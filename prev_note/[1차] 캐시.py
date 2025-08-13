from collections import deque
def solution(cacheSize, cities):
    # cache 라는 것은 자료구조를 어떻게 정의할까? 앞뒤로 넣꼬 빼는게 빨라야 하니까..
    class Cache:
        def __init__(self, size):
            self.cache = deque()
            self.size = size

        def is_full(self):
            return len(self.cache) == self.size

        def add(self, value):
            if self.size == 0:
                return
            if self.is_full():
                self.cache.popleft()
                self.cache.append(value)
                return
            self.cache.append(value)

        def hit(self, value):
            if value in self.cache:
                self.cache.remove(value)
                self.cache.append(value)
                return True
            else:
                self.add(value)
                return False

    cache = Cache(cacheSize)
    total_time = 0
    for city in cities:
        city = city.lower()
        if cache.hit(city):
            total_time += 1
        else:
            total_time += 5
    print("total_time: ", total_time)


solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])

# 재미있긴 한데 굳이 이렇게 클래스로 정의할 필요는 없을 것 같기도 하고..