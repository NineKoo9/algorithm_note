# import sys
# import heapq
#
# n = int(input())
# q = []
#
# for i in range(n):
#     a = int(sys.stdin.readline().rstrip())
#     if a != 0:
#         heapq.heappush(q, (abs(a), a))
#     else:
#         if not q:
#             print(0)
#         else:
#             print(heapq.heappop(q)[1])
#
#
def solution2():
    import heapq

    N = int(input())
    nums = [int(input()) for _ in range(N)]
    h = []
    for num in nums:
        if h and num == 0:
            abs_value, value = heapq.heappop(h)
            print(value)
        elif num == 0:
            print(0)
        else: # 추가
            heapq.heappush(h, (abs(num), num))

solution2()

