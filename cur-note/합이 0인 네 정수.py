from bisect import bisect_right, bisect_left
from collections import defaultdict
import sys

def solution():
    input = sys.stdin.readline

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 여기서부터 arr1과 arr2의 모든 합의 경우를 구한다.
    first_sum_result = []
    second_sum_result = []
    for i in range(n):
        for j in range(n):
            first_sum_result.append(arr[i][0] + arr[j][1])
            second_sum_result.append(arr[i][2] + arr[j][3])


    # 이제 더해진 결과를 기준으로 해당하는 값이 있는지 없는지 체크한다.
    # 단 중복이 있을 수 있으니... 그 부분은 따로 저장한다?
    duplicate_value = defaultdict(int)
    second_sum_result.sort()

    count = 0
    for value in first_sum_result:
        # 이제부터 second_sum_result의 결과에 마이너스를 한 녀석이 value에 해당하는지 체크해야한다.
        if value in duplicate_value:
            count += duplicate_value[value]
            continue
        hi = bisect_right(second_sum_result, -value)
        lo = bisect_left(second_sum_result, -value)
        duplicate_value[value] = hi - lo
        count += hi - lo

    print(count)

def solution2():
    input = sys.stdin.readline

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 여기서부터 arr1과 arr2의 모든 합의 경우를 구한다.
    first_sum_result = []
    second_sum_result = {}
    for i in range(n):
        for j in range(n):
            first_sum_result.append(arr[i][0] + arr[j][1])
            second_sum_result[arr[i][2] + arr[j][3]] = second_sum_result.get(arr[i][2] + arr[j][3], 0) + 1

    count = 0
    for value in first_sum_result:
        # 이제부터 second_sum_result의 결과에 마이너스를 한 녀석이 value에 해당하는지 체크해야한다.
        if -value in second_sum_result:
            count += second_sum_result[-value]

    print(count)

solution2()