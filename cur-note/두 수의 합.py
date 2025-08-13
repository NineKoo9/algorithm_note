def solution():
    n = int(input())
    array = list(map(int, input().split()))
    x = int(input())
    array.sort()
    s = 0
    e = 1
    count = 0
    while 0 <= s < e < n:
        if array[s] + array[e] == x:
            s -= 1
            e += 1
            count += 1
        elif array[s] + array[e] < x:
            s += 1
            e += 1
        else:  # array[s] + array[e] > x:
            s -= 1
    print(count)

def solution2():
    n = int(input())
    array = list(map(int, input().split()))
    x = int(input())

    # 지금부터 array의 2수의 합이 x가 되는 쌍을 구하면 된다!
    array.sort()
    s = 0
    e = 1
    count = 0
    while 0 <= s < e < n:
        a_1 = array[s]
        a_2 = array[e]
        if a_1 + a_2 < x:
            s += 1
            e += 1
        elif a_1 + a_2 == x:
            count += 1
            s -= 1
            e += 1
        else:  # a_1 + a_2 > x
            s -= 1
    print(count)

def solution3():
    n = int(input())
    array = list(map(int, input().split()))
    x = int(input())

    # Sort the array for the two-pointer technique
    array.sort()

    # Initialize pointers and count
    s = 0
    e = n - 1
    count = 0

    # Use two pointers to find pairs that sum to x
    while s < e:
        current_sum = array[s] + array[e]

        if current_sum < x:
            # Move the start pointer right to increase the sum
            s += 1
        elif current_sum > x:
            # Move the end pointer left to decrease the sum
            e -= 1
        else:
            # Found a pair that sums to x
            count += 1
            s += 1
            e -= 1

    print(count)

def solution4():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    A.sort()
    s = 0
    e = len(A) - 1
    count = 0
    while s < e:
        if A[s] + A[e] > X:
            e -= 1
        elif A[s] + A[e] < X:
            s += 1
        else:
            count += 1
            s += 1
            e -= 1
    print(count)
solution4()