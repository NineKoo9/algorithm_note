def solution():
    # 좌표를 압축했다면... 원래로 복원은 어케할까? 이분탐색!
    # 좌표압축으로 문제를 푸는 것일까?
    # N 은 10만까지고 시간은 100억이다
    # 계산이 겹치는 부분이 있다.(1, 4) (2, 6) (3, 7) (5, 9) (6, 8)
    # 이미 제거를 했다면... 그 뒷부분은 미리 계산해놓은 것을 메모이제이션 해놓을 수 있다?
    # 각 포인트를 0, 1, 2, 3, 4라 했을 때 2차원 배열로 아... 10만 * 10만인데...
    # 전체에서... 각 소가 단독으로 커버하는 시간을 빼면서 비교하면 되구나...
    # hmm... how should I calculate the solo convering interval?

    N = int(input())
    events = []
    for i in range(N):
        s, e = map(int, input().split())
        events.append((s, 1, i))
        events.append((e, -1, i))

    active_users = set()
    events.sort()
    # 이제부터 각 이벤트에 대해서 처리를 해나가자
    # 총 시간은 어떻게 구해야할까?
    # 그리고 솔로 커버링 시간은 어떻게?
    solo_covering_interval = [0] * N
    total_length = 0
    last_time = events[0][0]
    for t, state, guard_idx in events:
        time_delta = t - last_time
        if active_users:
            total_length += time_delta
            if len(active_users) == 1:
                lonely_guard_idx = next(iter(active_users))
                solo_covering_interval[lonely_guard_idx] = time_delta

        if state == 1:
            active_users.add(guard_idx)
        else:
            active_users.remove(guard_idx)
        last_time = t
    print(total_length - min(solo_covering_interval))
    

solution()