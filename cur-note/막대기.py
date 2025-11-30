def solution():
    import heapq
    
    X = int(input())
    
    polls = []
    heapq.heappush(polls, 64)
    while 1:
        if sum(polls) > X:
            min_poll = heapq.heappop(polls)
            divided_poll = min_poll // 2
            if sum(polls) + divided_poll >= X:
                heapq.heappush(polls, divided_poll)
            else:
                heapq.heappush(polls, divided_poll)
                heapq.heappush(polls, divided_poll)
        else:
            print(len(polls))
            break

solution()