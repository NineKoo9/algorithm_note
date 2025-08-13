def solution():
    N, K = map(int, input().split())
    enemies = [list(map(int, input().split())) for _ in range(N)]

    # 진수가 적어도 k명을 이기기 위해서는 어떻게 스탯을 가져야할까?
    str_set = {s for s, _, _ in enemies}
    dex_set = {d for _, d, _ in enemies}
    int_set = {i for _, _, i in enemies}
    min_stats = int(1e9)
    for s in str_set:
        for d in dex_set:
            for i in int_set:
                stats = s + d + i
                count = 0
                for e_s, e_d, e_i in enemies:
                    if s >= e_s and d >= e_d and i >= e_i:
                        count += 1
                if count >= K:
                    min_stats = min(min_stats, stats)
    print(min_stats)

solution()

# 완전 탐색을 어떤 방향으로 접근할 것인가가 중요하다. 적어도 K라는 조건이 있으니 조합으로 가는 것은 무리가 있다.
# 다른 방향으로 완전 탐색을 고려했더니 그 기준이 스탯이 되었다.