def solution():
    import sys
    
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split())) # nums 는 최대 100만 원소는 최대 10억
    nums_dic = {}
    for num in nums:
        nums_dic[num] = 1
    nums_sorted = sorted(nums_dic.keys())
    nums_order = {num:i for i, num in enumerate(nums_sorted)}
    compressed_result = []
    for num in nums:
        order = nums_order[num]
        compressed_result.append(str(order))
    print(" ".join(compressed_result))

def solution2():
    N = int(input())
    points = list(map(int, input().split()))
    sorted_points = sorted(list(set(points)))
    point_dic = {point:idx for idx, point in enumerate(sorted_points)}
    results = []
    for point in points:
        results.append(point_dic[point])
    print(*results)

def solution3():
    def binary_left(arr, n):
        s = 0
        e = len(arr) - 1
        ans = len(arr)
        while s <= e:
            mid = (s + e) // 2
            if arr[mid] < n:
                s = mid + 1
            else:  # mid >= n
                ans = mid
                e = mid - 1
        return ans

    N = int(input())
    numbers = list(map(int, input().split()))

    sorted_distinct_numbers = sorted(set(numbers))
    compressed_points = [binary_left(sorted_distinct_numbers, num) for num in numbers]
    print(*compressed_points)


solution3()

