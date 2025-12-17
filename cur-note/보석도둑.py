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

# 나의 생각은 가방 하나에 최대의 가치가 들어가면 된다. 무게 제한이 c라면?
# C이하의 무게에서 최대 value을 넣으면 된다고 까지 생각했다.
# 그러나 여기서... 최대 value을 찾는것을 바로 이분탐색으로 생각했다.
# 생각이 더 나아가야했다. C이하의 무게에서 최대 value을 찾지만... 그 이후도 생각해보자
# 그 다음 크기의 가방에도 D(C < D) 이하의 무게에서 또 최대의 value을 찾아야했다.
# 당연히 C에 들어갈 수 있던 보석들? D에도 들어갈 수 있다.
# 이게 이 문제의 핵심이다. 
def solution2():
    import heapq

    N, K = map(int, input().split())
    jewels = [list(map(int, input().split())) for _ in range(N)]
    bag_size_lst = [int(input()) for _ in range(K)]

    # 가장 뒤에 있는 보석의 무게가 가장 작다
    jewels.sort(key=lambda jewel: -jewel[0])
    bag_size_lst.sort()

    # 가방의 무게가 작은 것 부터 탐색을 한다.
    pq = []
    answer = 0
    for bag_size in bag_size_lst:
        # bag_size 이하의 모든 보석을 찾아서 우선순위큐에 넣어준다.
        while jewels and jewels[-1][0] <= bag_size:
            jewel_weight, jewel_value = jewels.pop()
            heapq.heappush(pq, (-jewel_value, jewel_weight))
        
        # 찾은 보석들 중에서 가장 가치가 높은 녀석을 가방에 담는다
        if pq:
            minus_jewel_value, jewel_weight = heapq.heappop(pq)
            jewel_value = -1 * minus_jewel_value
            answer += jewel_value
    print(answer)

solution2()