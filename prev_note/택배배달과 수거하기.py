def solution(cap, n, deliveries, pickups):  # 1<=cap<=50 n은 최대 10만개
    # 최소 이동거리를 어떻게 계산할까?
    acc_sum_deliveries = [0] * n
    acc_sum_pickups = [0] * n
    print(acc_sum_pickups)
    for i in range(n):
        if i == 0:
            acc_sum_deliveries[i] = deliveries[0]
            acc_sum_pickups[i] = pickups[0]
            continue
        acc_sum_deliveries[i] = acc_sum_deliveries[i - 1] + deliveries[i]
        acc_sum_pickups[i] = acc_sum_pickups[i - 1] + pickups[i]

    print(acc_sum_deliveries)
    print(acc_sum_pickups)

    result = []
    cur_cap = cap  # 캡을 늘린다는 생각을 왜 못했을까...?
    point = -1
    for i in range(n):
        point = i
        while acc_sum_deliveries[point] > cur_cap and acc_sum_pickups[point] > cur_cap:
            result.append((point) * 2)
            cur_cap += cap
        # 그렇다면 여기서 마지막인 경우는?
        if i == n - 1:
            result.append((point + 1) * 2)
    print(result)
    return sum(result)


# 위의 풀이는 내가 풀다가 포기한 풀이 솔류션2가 정답 찾아본 풀이
def solution2(cap, n, deliveries, pickups):
    answer = 0
    delivery_sum = 0
    pickup_sum = 0

    for i in range(n - 1, -1, -1):
        cnt = 0
        delivery_sum += deliveries[i]
        pickup_sum += pickups[i]

        while delivery_sum > 0 or pickup_sum > 0:
            delivery_sum -= cap
            pickup_sum -= cap
            cnt += 1

        answer += (i + 1) * 2 * cnt

    return answer

