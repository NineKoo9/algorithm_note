def solution():
    N, M = map(int, input().split())
    no_listen_set = {input() for _ in range(N)}
    no_seen_set = {input() for _ in range(M)}
    answer = no_listen_set & no_seen_set
    print(len(answer))
    for name in sorted(answer):
        print(name)

solution()