def solution():
    n = int(input()) # n은 26억까지 갈 수 있다
    # 이것을... 최대 21억까지 연산하는것은 너무 크다.
    # 다른 방법을 생각해보자.
    i = 1
    while 1:
        if i**2 <= n < (i+1)**2:
            print(i)
            break
        i += 1

def solution2():
    import math
    N = int(input())

    print(int(math.sqrt(N)))

solution2()