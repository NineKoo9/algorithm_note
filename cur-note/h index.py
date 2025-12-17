def binary_right(arr, n):
    ans = len(arr)
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= n:
            start = mid + 1
        else: # arr[mid] < n 이라면
            ans = mid
            end = mid - 1
    return ans

def solution(citations):
    n = len(citations)
    citations.sort(reverse = True)
    max_h = 0
    for h in range(citations[0]):
        # h이상인 녀석들의 수를 구한다.
        count = binary_right(citations, h)
        # 이제 조건을 확인한다.
        if count >= h:
            max_h = max(max_h, h)
    return max_h