import heapq

def solution():
    N, K = map(int, input().split())  # 보석 n개 가방 k개
    jewel_lst = [tuple(map(int, input().split())) for _ in range(N)]
    bag_lst = [int(input()) for _ in range(K)]

    jewel_lst.sort(reverse=True)
    bag_lst.sort()

    pq = []
    result = 0
    for bag_size in bag_lst:
        while jewel_lst and jewel_lst[-1][0] <= bag_size:
            jewel_weight, jewel_value = jewel_lst.pop()
            heapq.heappush(pq, (-jewel_value, jewel_weight))

        if pq:
            minus_jewel_value, jewel_weight = heapq.heappop(pq)
            result += -1 * minus_jewel_value

    print(result)

solution()