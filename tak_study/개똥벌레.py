def solution():
    N, H = map(int, input().split())
    imos = [0] * H
    for i in range(N):
        stick = int(input())
        if i % 2 != 0:
            if H - stick >= 0:
                imos[H - stick] += 1
        else:
            imos[0] += 1
            if stick < H:
                imos[stick] -= 1

    for i in range(1, H):
        imos[i] += imos[i - 1]
    min_value = min(imos)
    count = imos.count(min_value)
    print(min_value, count)


solution()