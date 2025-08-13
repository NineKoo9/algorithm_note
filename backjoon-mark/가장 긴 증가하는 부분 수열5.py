import sys
import bisect


def solve():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    # 꼬리값 리스트 (수열 값들을 직접 저장)
    lis = []
    # 길이가 i일 때, 마지막 원소가 되는 인덱스
    lis_indices = [0] * N
    # i번째 원소 바로 앞에 오는 원소 인덱스(역추적용)
    parent = [-1] * N

    length = 0  # lis의 현재 길이
    for i in range(N):
        # A[i]가 들어갈 위치 idx를 이진탐색으로 찾는다
        idx = bisect.bisect_left(lis, A[i])

        # idx가 lis의 길이면 => 더 긴 LIS를 만들 수 있음
        if idx == length:
            lis.append(A[i])
            lis_indices[idx] = i
            length += 1
        else:
            # 아니라면 => lis[idx]를 더 작은 값으로 교체
            lis[idx] = A[i]
            lis_indices[idx] = i

        # 역추적을 위해 parent 정보 업데이트
        # idx > 0 이어야 앞에 오는 원소가 존재하므로
        if idx > 0:
            parent[i] = lis_indices[idx - 1]

    # 이제 length가 '가장 긴 증가부분수열'의 길이
    # 그 마지막 원소의 인덱스는 lis_indices[length-1]
    lis_end_index = lis_indices[length - 1]

    # 거기서부터 parent를 거슬러 올라가면서 수열을 찾는다
    answer = []
    cur = lis_end_index
    while cur != -1:
        answer.append(A[cur])
        cur = parent[cur]

    # 뒤에서부터 모았으니 뒤집어준다
    answer.reverse()

    # 출력
    print(length)
    print(*answer)


solve()
