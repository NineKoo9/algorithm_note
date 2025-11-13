def solution():
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    cards.sort()
    total_result = 0
    prev_sum = cards[0]
    for card in cards[1:]:
        prev_sum += card
        total_result += prev_sum
    print(total_result)


# 첫번째 풀이인 단순히 정렬해서 작은거부터 더하는 방식으로는 안되는 거엿다.

def solution2():
    import sys
    import heapq

    input = sys.stdin.readline

    n = int(input())
    cards = []
    for i in range(n):
        heapq.heappush(cards, int(input()))

    result = 0

    if len(cards) == 1:
        print(result)

    else:
        for i in range(n - 1):  # 2개씩 꺼내기 떄문에 n-1
            previous = heapq.heappop(cards)
            current = heapq.heappop(cards)

            result += previous + current
            heapq.heappush(cards, previous + current)

        print(result)

def solution3():
    import heapq

    # 최소한 몇번의 비교가 필요한지 구해야한다.
    N = int(input())
    cards = [int(input()) for _ in range(N)]

    # a < b < c 이 순서가 항상 보장되어야 한다.
    # 아 이거 누적 덧셈 어케 할지 계속 막히네... 구현이...
    if len(cards) == 1:
        print(0)
    else:
        heapq.heapify(cards)
        answer = 0
        while len(cards) > 1:
            prev = heapq.heappop(cards)
            cur = heapq.heappop(cards)
            answer += prev + cur
            heapq.heappush(cards, prev + cur)
        print(answer)


solution3()