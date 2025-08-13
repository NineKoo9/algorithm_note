def solution():
    def div_conq(block_size, y, x):
        # 길이가 1이 되면, 해당 색깔을 반환한다.
        if block_size == 1:
            return M[y][x]
        block_size = block_size // 2
        r1 = div_conq(block_size, y, x)
        r2 = div_conq(block_size, y,  x + block_size)
        r3 = div_conq(block_size, y + block_size, x)
        r4 = div_conq(block_size, y + block_size, x + block_size)
        # 모든 색깔이 같다면? 합쳐서 종이 하나로 한다.
        if r1 == r2 == r3 == r4:
            return r1
        # 하나라도 다르면 다 낱개이지
        if r1 is not None :
            color_count[r1] += 1
        if r2 is not None:
            color_count[r2] += 1
        if r3 is not None:
            color_count[r3] += 1
        if r4 is not None:
            color_count[r4] += 1
            
    N = int(input())
    M = [tuple(map(int, input().split())) for _ in range(N)]
    color_count = [0, 0] # white는 0번 blue는 1번으로 하자.
    r1 = div_conq(N, 0, 0)
    if r1 is not None:
        color_count[r1] += 1
    print(*color_count, sep="\n")


solution()