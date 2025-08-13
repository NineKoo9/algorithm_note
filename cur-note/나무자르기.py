def solution():
    def get_tree(h):
        result = 0
        for height in heights:
            if height - h >= 0:
                result += height - h
        return result
    
    N, M = map(int, input().split()) # N은 나무의 수 100만개가 최대, M 은 가져갈려는 길이 최대 10억
    heights = list(map(int, input().split()))
    heights.sort()
    min_len = 0
    max_len = heights[-1] + 1
    while min_len + 1 < max_len:
        mid = (min_len + max_len) // 2
        if get_tree(mid) >= M:
            min_len = mid
        else:
            max_len = mid
    print(min_len)

solution()