def solution():
    N = int(input())
    liquids = list(map(int, input().split()))
    liquids.sort()

    min_three_sum = int(1e10)
    result = (0, 0, 0)
    # 이 방법... 내 생각으로 대략 시간복잡도가 최대 5천만인데...
    for start in range(N):
        mid = start + 1
        end = N - 1
        while start < mid < end:
            three_sum = liquids[start] + liquids[mid] + liquids[end]
            if abs(three_sum) < min_three_sum:
                min_three_sum = abs(three_sum)
                result = (liquids[start], liquids[mid], liquids[end])

            if three_sum == 0:
                print(liquids[start], liquids[mid], liquids[end])
                exit()
            elif three_sum > 0:
                end -= 1
            elif three_sum < 0:
                mid += 1
    print(*result)

solution()