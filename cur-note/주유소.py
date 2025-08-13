def solution():
    N = int(input())
    road_length = list(map(int, input().split()))
    node_price = list(map(int, input().split()))
    visited = [0] * N
    total_cost = 0
    for i in range(N - 1):
        if visited[i]:
            continue
        visited[i] = 1
        length = road_length[i]
        price = node_price[i]
        tmp = i + 1
        while tmp < N - 1 and node_price[i] < node_price[tmp]:
            # 다음 녀석이 더 비싸다면.. 최대한 그 거리까지 여기서 다 채운다
            length += road_length[tmp]
            visited[tmp] = 1
            tmp += 1
        total_cost += length * price
    print(total_cost)

def solution2():
    N = int(input())
    dists = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    min_cost = 0
    visited = [0] * len(dists)
    for i in range(len(dists)):
        if visited[i]:
            continue
        visited[i] = 1
        dist = dists[i]
        price = prices[i]
        min_cost += dist * price
        next_i = i + 1
        while next_i < len(dists) and prices[next_i] > price:
            visited[next_i] = 1
            min_cost += price * dists[next_i]
            next_i += 1
    print(min_cost)

def solution3():
    N = int(input())  # 최대 10만개
    roads = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    cost = 0
    min_price = prices[0]
    for i in range(N - 1):
        dist = roads[i]
        price = prices[i]
        if price < min_price:
            min_price = price
        cost += dist * min_price
    print(cost)

solution3()