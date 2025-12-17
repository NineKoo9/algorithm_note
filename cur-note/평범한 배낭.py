from itertools import product


def solution():
    N, K = map(int, input().split()) # 갯수, 최대 버틸수있는 무게 K
    objects = [tuple(map(int, input().split())) for _ in range(N)]
    # 또 다른 정보하나가 필요하겠다. 특정 무게를 인덱스로 가지고 그 무게에 해당하는 가치가 
    w_obj = {w:value for w, value in objects}
    
    objects.sort() # (무게, 가치)
    print(objects)
    print(w_obj)
    INF = int(1e9)
    dp = [-INF] * (K + 1)
    for w in range(K + 1):
        for obj_weight, obj_value in sorted(w_obj.items()):
            if obj_weight < w and (dp[w - obj_weight] != -INF):
                dp[w] = max(dp[w], dp[w - obj_weight] + obj_value) # i무게일때의 최대 가치과 그 i 무게에 해당하는 녀석의 가치
            elif obj_weight == w:
                dp[w] = max(dp[w], obj_value)
            elif obj_weight > w:
                break
    print(dp)
    print(dp[K])

# 아 중복이 발생할 수 있구나 
# 어떤 물건을 넣었는지 체크할 필요가 있다. 완전히 탐색해 나갈까? 어떤 물건이 있고 없고는 2^100이 되므로 불가능이다.
# 하지만... 기록해나갈 방법이 있을까?특정 가격의 최대에서 어떤 물건이 있고 없고를 기록해 나간다?
def solution2():
    N, K = map(int, input().split()) # 갯수, 최대 버틸수있는 무게 K
    objects = [tuple(map(int, input().split())) for _ in range(N)]
    objects.sort()
    dp = [[0] * len(objects) for _ in range(K + 1)] # 어떤 아이템이 있고 없고가 아니라... j번째 물건 까지 물건을 살펴보았는지 안되었는지를 기준으로 간다.
    for w in range(1, K + 1):
        for j in range(len(objects)):
            object_weight, object_value = objects[j]
            # 만약에 j가 0인 경우는 어떻게 처리할까? 0번째 까지 고려되었을때 무게 w의 최대값은? 
            if w < object_weight: # 현재 담을려는 총 무게보다 물체의 무게가 더 크다면 담을수가 없다 그렇다면 그 값은 무엇이 되지? 그 전 무게까지가 고려대상이다.
                dp[w][j] = dp[w][j - 1] if j - 1 >= 0 else 0 # j도 0이고 물건도 담을수없다면 가치는 0이지
            elif w >= object_weight:
                if j == 0: # 현재 고려하는 물건을 담을수있고.. 그녀석이 첫번째(0번째) 녀석이라면 바로 그 가치를 가진다.
                    dp[w][j] = object_value
                    continue
                dp[w][j] = max((dp[w - object_weight][j - 1] + object_value), dp[w][j - 1]) # dp[w][j] 을 새롭게 업데이트해나갈 필요는 없지... 
    print(max(dp[K]))

def solution3():
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    items.sort(key=lambda item: item[0])
    print(items)
    dp = [[0] * N for _ in range(K + 1)]
    for weight in range(K + 1):
        for idx, item in enumerate(items):
            item_weight, value = item
            if item_weight > weight:
                dp[weight][idx] = max(dp[weight][idx], dp[weight][idx - 1] if idx - 1 >= 0 else 0)
            elif item_weight == weight:
                dp[weight][idx] = max(dp[weight][idx - 1], value)
            else: # item_weight < weight
                dp[weight][idx] = max(dp[weight - item_weight][idx - 1] + value if idx - 1 >= 0 else 0,
                                      dp[weight - 1][idx],
                                      dp[weight][idx - 1] if idx - 1 >= 0 else 0)
    print(max(dp[K]))

def solution4():
    N, K = map(int, input().split())
    products = [tuple(map(int, input().split())) for _ in range(N)]
    products.sort()  # 무게를 기준으로 정렬한다.
    dp = [[0] * N for _ in range(K + 1)]  # 여기는 value을 담는다.
    for bag_max_weight in range(1, K + 1):
        for i in range(N):
            product_weight = products[i][0]
            product_value = products[i][1]
            if product_weight > bag_max_weight:
                dp[bag_max_weight][i] = max(dp[bag_max_weight][i], dp[bag_max_weight][i - 1] if i - 1 >= 0 else 0)
            elif product_weight <= bag_max_weight:
                dp[bag_max_weight][i] = max(dp[bag_max_weight][i],
                                            dp[bag_max_weight][i - 1] if i - 1 >= 0 else 0,
                                            product_value + (dp[bag_max_weight - product_weight][i - 1] if i - 1 >= 0 else 0 ))
    print(max(dp[K]))

solution4()