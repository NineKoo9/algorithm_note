def solution():
    n = int(input())  # 2 이상 10만 이하
    arr = list(map(int, input().split()))
    arr.sort()
    s = 0
    e = 1
    min_diff = int(2e9)
    answer = []
    # 자 여기서 두 용액의 합이 0과 최대한 가까워야 한다. 그 말인 즉슨 abs(0 - (arr[i] + arr[j])) 가 최소값이 되는 지점을 찾으면 된다.
    #  그럴려면... 두개의 합이 최소가 되는 곳을 찾아야 겠구나?가 아니라... 0 에 가까워야 겠네
    # 정렬과 투포인터를 사용하는 이유는 불필요한 경우를 탐색하지 않기 위함이다.
    while 0 <= s < e < n:
        sum_value = arr[s] + arr[e]
        if abs(0 - sum_value) < min_diff:
            min_diff = abs(0 - sum_value)
            answer = [arr[s], arr[e]]
        if sum_value < 0:
            s += 1
            e += 1
        elif sum_value > 0:
            s -= 1
        else:  # s == 0 이라면 정답 그 자체이다
            answer = [arr[s], arr[e]]
            break


    print(*answer)

def solution2():
    N = int(input())
    array = list(map(int, input().split()))
    array.sort()

    # 이제부터 0에 가장 가까운 쌍을 찾아야 한다. -> 절댓값이 가장 작은 쌍을 찾아야한다.
    # 그렇다면 절댓값?
    # 양쪽에서 가면은...
    # 0에 가장 가까운 수를 어떻게 만들어낼까? 어쨋든 두개를 더해야하고 그 값을 비교해야한다. 무엇이랑?
    # 아... 결국엔 0에 가장 가까워져야 하는 것이고... 그 과정에서 최대한 가까운 녀석을 찾는 것이다.
    s = 0
    e = 1
    min_value = int(3e10)
    answer_pair = None
    while 0 <= s < e < N:
        l_1 = array[s]
        l_2 = array[e]
        sum_value = l_1 + l_2
        if abs(sum_value) < min_value:
            min_value = abs(sum_value)
            answer_pair = (l_1, l_2)
        if sum_value == 0:
            print(l_1, l_2)
            exit()
        elif sum_value < 0:
            s += 1
            e += 1
        else:
            s -= 1

    print(*answer_pair)

def solution3():
    N = int(input())
    A = list(map(int, input().split()))

    # 먼저 정렬을 한다.
    A.sort()

    s = 0
    e = len(A) - 1

    min_value = int(2e10)
    min_pair = (A[s], A[e])
    while s < e:
        sum_value = A[s] + A[e]
        if min_value > abs(sum_value):
            min_value = abs(sum_value)
            min_pair = (A[s], A[e])

        if sum_value > 0:
            # 줄이는 방향으로 가야지?
            e -= 1
        elif sum_value < 0:
            s += 1
        elif sum_value == 0:
            # 이건 정답 별견이지.. 탐색끝내도된다.
            s += 1
            e -= 1
    print(*min_pair)

solution3()