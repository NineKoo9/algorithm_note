def solution():
    def check(x) -> bool:
        # 최저 거리를 x로 잡았을때 설치할 수 있는 공유기의 갯수를 구하는 함수를 정의해야한다.
        # 이것을 반대로... 최저 거리를 x로 잡았을때 삭제해야할 집의 갯수를 구하고... 남아있는 집의 수와 C을 비교하면 어떨까?
        # 현재 이것을 잘못 구하였는데...
        count = 0 # 이 녀석은 C 보다 1 작은 녀석이 만족하면 트루 아니면 거짓
        s_point = 0
        e_point = 1
        # 투 포인터로 찾아간다.
        while s_point < e_point and e_point < N:
            if house_points[e_point] - house_points[s_point] >= x:
                count += 1
                if count + 1 >= C:
                    return True
                s_point = e_point
            e_point += 1
        return False
    
    N, C = map(int, input().split()) # N은 최대 20만
    house_points = [int(input()) for _ in range(N)] #최대 값이 10억개
    house_points.sort()
    lo = 1
    hi = house_points[-1] - house_points[0] + 1 # 2 2 1 2 인 경우와 같이... lo 와 hi 의 결과가 같은 경우가 있다. 그것을 방지하기 위함.
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo) # 가장 의문이 남는 것은... lo가 어떻게 그 사이 거리에 존재하는 것을 보장하는가 이다. 어쨋든 lo 도 mid을 통해서 왔기때문에..
    # 탐색할때 mid 을 기준으로 잡으면 그 녀석의 거리가 존재하는지? 확신할 수 있는가? 아니 mid거리가 진정 최소가 되는 것을 확실한가? 더 큰 거리가 있을 수 있지 않나?
    # 그렇다면 그 더 큰 거리가 mid 로 잡힐수도 있지 않을까? 그렇다면... lo=mid 을 하여 더 큰 mid을 찾아나갈 것이다. 이것을 극한으로 반복하면 결국에 딱 맞는 값이 나오는 것일까? 결국 정답에 해당하는 mid가 존재한다는 가정을 통해서
    # 찾는것이니까 그런걸까?

solution()