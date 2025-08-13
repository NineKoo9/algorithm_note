def solution():
    import math
    
    N = int(input())
    garosu_lst = [int(input()) for _ in range(N)]
    distances = [garosu_lst[i+1] - garosu_lst[i] for i in range(N-1)]
    gcd = math.gcd(*distances)
    num_of_dis = (garosu_lst[-1] - garosu_lst[0]) // gcd 
    num_of_garosu = num_of_dis + 1 - len(garosu_lst)
    print(num_of_garosu)


def solution2():
    import math

    N = int(input())
    tree_points = [int(input()) for _ in range(N)]
    distances = [tree_points[i + 1] - tree_points[i] for i in range(N - 1)]
    g = math.gcd(*distances)
    print(g)
    # 그렇다면 이렇게 나온 값을 심는다면 몇개가 필요하냐?
    print((tree_points[-1] - tree_points[0]) // g - N + 1)


# 이러한 이분탐색 풀이는 잘못된 것이다.
def solution3():

    # 이 함수의 역할은 m의 거리로 했을 때 가로수를 심을 수 있냐 없냐를 구하면 되겠다.
    def check(m):

        # 아아... 이거 트리가 아니라 트리의 절대위치이지...
        for i in range(len(trees) - 1):
            c = trees[i]
            n = trees[i + 1]
            if (n - c) % m != 0:
                return False
        return True

    N = int(input())
    trees = [int(input()) for _ in range(N)]
    # 이 문제 이분탐색으로도 가능하겠다.

    start = 1 # 1을 거리로 잡는다면 모든 경우가 가능할 것이다. 다만 가로수의 수가 많을 것
    end = max([trees[i+1] - trees[i] for i in range(N - 1)])
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid):
            start = mid
        else:
            end = mid
    # 자 여기서 start는 최소의 거리가 될 것이다.
    # 그렇다면 가로수는 몇개를 구해야하나?
    answer = 1 + (trees[-1] - trees[0]) // start - len(trees)
    print(answer)

solution3()