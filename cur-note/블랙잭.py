def solution():
    # N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력
    # 카드는 최대 100개 이다. 여기서 3장을 무작위로 고른다 했을때... M에 최대한 가까운 합을 구하란 것이군
    N, M = map(int, input().split())
    cards = sorted(list(map(int, input().split())))
    min_diff = int(1e9)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                three_sum = cards[i] + cards[j] + cards[k]
                if three_sum > M:
                    break
                min_diff = min(min_diff, M - three_sum)
    print(M-min_diff)


solution()
# 아하 중복되는 것이 발생하는 구나? 중복없는 조합을 구해야 하네.